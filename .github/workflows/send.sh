if [[ $CLIENT == "google" ]]; then
  python3 .github/workflows/send_google.py "$@"
elif [[ $CLIENT == "aws" ]]; then
  python3 .github/workflows/send_aws.py "$@"
else
  echo "Plataforma desconhecida: $CLIENT"
fi