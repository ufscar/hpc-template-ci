if [[ $CLIENT == "google" ]]; then
  python3 .gitlabci/send_google.py "$@"
elif [[ $CLIENT == "aws" ]]; then
  python3 .gitlabci/send_aws.py "$@"
else
  echo "Plataforma desconhecida: $CLIENT"
fi