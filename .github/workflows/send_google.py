import os
import io
import re
import base64
import json, pickle
import mimetypes

from datetime import datetime as dt2

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

COLLECTION_CONTAINER = os.getenv('COLLECTION_CONTAINER', 'collection/container')
COLLECTION = '/'.join(COLLECTION_CONTAINER.split('/')[:-1])
CONTAINER = COLLECTION_CONTAINER.split('/')[-1]
CREDENTIALS = os.getenv('CREDENTIALS', '').strip()
if CREDENTIALS == '':
    print('''ERRO! Favor definir a variável de ambiente CREDENTIALS com o resultado de
    python3 get_google_token.py
executado localmente''')
CREDENTIALS = base64.b64decode(CREDENTIALS)


def service():
    with io.BytesIO(CREDENTIALS) as cred_file:
        creds = pickle.load(cred_file)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print('''ERRO! Favor redefinir a variável de ambiente CREDENTIALS com o resultado de
    python3 get_google_token.py
executado localmente''')
            return None
    return build('drive', 'v3', credentials=creds)


def exists_folder(folder, parent, serv):
    response = None
    try:
        response = serv.files().list(
            q=f"name='{folder}' and '{parent}' in parents "
              f"and mimeType='application/vnd.google-apps.folder' and trashed=false",
            spaces='drive'
        ).execute()
        return response['files'][0]['id']
    except Exception as err:
        print(f'exists_folder() - {err}\n{response}')
        return ''


def create_folder(fn, parent, serv):
    folder = serv.files().create(body={
        'name': fn,
        'parents': [parent],
        'mimeType': 'application/vnd.google-apps.folder'
    },
        fields='id').execute()
    return folder.get('id')


def upload(fn: str, serv) -> str:
    try:
        folders = ['openhpc', 'containers']+COLLECTION.split('/')
        id = 'root'
        for folder in folders:
            nid = exists_folder(folder, id, serv)
            if len(nid) == 0:
                nid = create_folder(folder, id, serv)
            id = nid
        mt = mimetypes.guess_type(fn, strict=False)[0]
        media = MediaFileUpload(fn, mimetype=mt)
        hj = re.sub(r'\D', '', str(dt2.now()))
        f = serv.files().create(media_body=media,
                                body={"name": fn.split(os.sep)[-1]+hj,
                                      "mimeType": mt,
                                      "parents": [id]},
                                fields='id').execute()
        return f"https://drive.google.com/open?id={f.get('id')}"
    except Exception as err:
        print(f'upload() - {err}')


def parse_files(args):
    if len(args) == 1:
        files_to_send = ['Singularity', 'Singularity.simg']
    else:
        files_to_send = args[1:]
    return list(filter(lambda x: os.path.exists(x), files_to_send))


if __name__ == '__main__':
    import sys
    files_to_send = parse_files(sys.argv)
    serv = service()
    for file in files_to_send:
        upload(file, serv)