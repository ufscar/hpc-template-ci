import base64
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pathlib import Path

SCOPES = ['https://www.googleapis.com/auth/drive']
SECRETS = os.path.join(str(Path.home()), '.secrets', '.google')
TOKEN_FILE = os.path.join(SECRETS, '.token')
CREDENTIALS_FILE = os.path.join(SECRETS, '.credentials')


def main():
    if not os.path.exists(CREDENTIALS_FILE):
        print(f'Copie o arquivo obtido das credenciais do Google API para {CREDENTIALS_FILE}:')
        print(f'\tcp /caminho/para/credenciais.json {CREDENTIALS_FILE}')
        return
    creds = None
    if not os.path.exists(SECRETS):
        os.makedirs(SECRETS)
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0, authorization_prompt_message='')
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    with open(TOKEN_FILE, 'rb') as token:
        TOKEN_FILE_content = token.read()

    cred = pickle.loads(TOKEN_FILE_content)
    print(f'''Para uso de input/output, acesse o cluster e execute o comando "rclone config" e forneça as seguintes informações quando solicitado:
n/s/q> n
name> nome para o perfil, a sua escolha
Storage> 13
client_id> {cred._client_id}
client_secret> {cred._client_secret}
scope> 1
root_folder_id> deixe em branco
service_account_file> deixe em branco
y/n> deixe em branco
y/n> n

Copie o url e cole no navegador no computador local. Autorize e:

Enter verification code> código fornecido pelo navegador após autorização
y/n> deixe em branco
y/e/d> deixe em branco
e/n/d/r/c/s/q> q

Para uso da disponibilização automática, salve esse conteúdo na variável de ambiente CREDENTIALS nas configurações de CI/CD do github.com: 
{str(base64.b64encode(TOKEN_FILE_content), encoding='ascii')}
''')


if __name__ == '__main__':
    main()