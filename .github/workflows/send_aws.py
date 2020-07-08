import os
import re

from datetime import datetime as dt2

import boto3    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
from botocore.exceptions import ClientError

from typing import Any, Tuple, List

COLLECTION_CONTAINER = os.getenv('COLLECTION_CONTAINER', 'collection/container')
ACCESS_KEY = os.getenv('ACCESS_KEY_AWS', '').strip()
SECRET_KEY = os.getenv('SECRET_KEY_AWS', '').strip()
if '' in [ACCESS_KEY, SECRET_KEY]:
    print('''ERRO! Favor definir as variáveis ACCESS_KEY_AWS e SECRET_KEY_AWS conforme explicado em README.md''')
    exit(0)


def service(region: str = 'sa-east-1') -> Tuple[Any, str]:
    s3 = boto3.client('s3',
                      region_name=region,
                      aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    return s3, create_bucket(s3)


def create_bucket(serv: Any, bucket_name: str = 'openhpc') -> str:
    buckets = serv.list_buckets()['Buckets']
    bucket_names = [b["Name"] for b in buckets]
    if bucket_name not in bucket_names:
        try:
            location = {'LocationConstraint': serv.meta.region_name}
            serv.create_bucket(Bucket=bucket_name,
                               CreateBucketConfiguration=location)
        except ClientError as err:
            print(err)
            return ''

    return bucket_name


def upload(fn: str, serv: Any, bucket: str) -> bool:
    folders = ['containers']+COLLECTION_CONTAINER.split('/')
    hj = re.sub(r'\D', '', str(dt2.now()))
    f, e = os.path.splitext(fn)
    f = os.path.split(f)[1]
    object_name = '/'.join(folders+[f+hj+e])

    try:
        serv.upload_file(fn, bucket, object_name)
    except ClientError as err:
        print(err)
        return False
    return True


def parse_files(args: List[str]) -> List[str]:
    if len(args) == 1:
        files_to_send = ['Singularity', 'Singularity.simg']
    else:
        files_to_send = args[1:]
    return list(filter(lambda x: os.path.exists(x), files_to_send))


if __name__ == '__main__':
    import sys
    files_to_send = parse_files(sys.argv)
    s3, bucket = service()
    for file in files_to_send:
        upload(file, s3, bucket)
