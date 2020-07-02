if [[ $# -lt 1 ]]; then
  echo "Usage: send.sh <plataforma> <arquivo1> <arquivo2>..."
  exit
fi

plat=$1
shift
if [[ $plat == "google" ]]; then
  python3 .github/send_google.py "$@"
else
  echo "Plataforma desconhecida: $plat"
fi