#!/bin/bash

apk add python3
apk add py3-pip
apk add curl

if [[ $CLIENT == "google" ]]; then
  pip3 install oauth2client
  pip3 install google-api-python-client
elif [[ $CLIENT == "aws" ]]; then
  pip3 install boto3
else
  echo "Plataforma desconhecida: $CLIENT"
fi