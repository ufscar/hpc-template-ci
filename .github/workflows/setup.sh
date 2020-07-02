#!/bin/bash

apk add python3
apk add py3-pip
apk add curl

pip3 install oauth2client
pip3 install google-api-python-client