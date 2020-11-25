echo "Criando imagem singularity... ${RECIPE}"
sudo echo 1 > /proc/sys/kernel/unprivileged_userns_clone
sudo singularity build -F "${RECIPE}.simg" "${RECIPE}"

echo "Configurando ambiente..."
if [[ -z $COLLECTION_CONTAINER ]]; then
  COLLECTION_CONTAINER=collection/container
fi
RCLONE_FILE=~/.config/rclone/rclone.conf
mkdir -p "$(dirname "${RCLONE_FILE}")"

echo "Configurando rclone..."
echo "${RCLONE_CONF}" | base64 -d >> "${RCLONE_FILE}"

echo "Enviando arquivos..."
files=( "${RECIPE}" "${RECIPE}.simg" )
NOW=$(date +'%Y%m%d%H%M%S')
for filename in "${files[@]}"; do
  if [[ -f $filename ]]; then
    path="$(dirname "${filename}")"
    filename="$(basename "${filename}")"
    if [[ "$filename" == *.* ]]; then
      dest="${filename%.*}_${NOW}.${filename##*.}"
    else
      dest="${filename}_${NOW}"
    fi
    rclone copyto "${path}/${filename}" "cloud:hpc/containers/${COLLECTION_CONTAINER}/${dest}"
  fi
done
