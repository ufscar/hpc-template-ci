# Template Integração Contínua Github

Esse projeto o template para uso do cluster da UFSCar, contendo integração contínua com o Google Drive e Amazon S3.

## Requisitos para Google Drive

1. Entre no [console de credenciais de API do Google](https://console.developers.google.com/apis/credentials)
2. Se ainda não houver um projeto, crie um com permissão para a "Google Drive API".
3. Clique em "Criar credenciais".
4. Selecione "ID do cliente do OAuth".
5. Em "Tipo de aplicativo", selecione "App para computador".
6. Dê um nome de identificação para as credenciais e clique em "criar".
7. Clique em "OK".
8. Clique no último botão na linha da credencial criada (seta para baixo) e salve o arquivo em um local seguro.
9. No computador, copie o arquivo para ~/.secrets/.google/.credentials (arquivo com nome .credentials).
10. Execute o script `python3 get_google_token.py`.
11. Adicione o conteúdo indicado na saída na variável de ambiente CREDENTIALS_GOOGLE no github (projeto >> Settings >> Secrets >> New Secret).
12. Adicione no github à variável COLLECTION_CONTAINER `/path/to/project`, esse será o caminho cujo container vai ser disponibilizado no seu Google Drive no formato `recipe_nameDateTime.simg`.
13. Acessar o site da [Sylabs Cloud](cloud.sylabs.io), criar um _access token_, copiar e adicionar na variável SYLABS_TOKEN no github.
14. Adicione no github à variável CLIENT `google`.


## Requisitos para Amazon S3

1. Entre na [AWS](console.aws.amazon.com)
2. Clique na seta ao lado de seu nome de usuário e em "My Security Credentials".
3. Na seção "Access Keys", clique em "Create New Access Key".
4. Na janela que aparece, clique em "Show Access Key".
5. Copie o conteúdo de "Access Key ID" na variável ACCESS_KEY_AWS no github (projeto >> Settings >> Secrets >> New Secret).
6. Copie o conteúdo de "Secret Access Key" na variável SECRET_KEY_AWS no github.
7. Acessar o site da [Sylabs Cloud](cloud.sylabs.io), criar um _access token_, copiar e adicionar na variável SYLABS_TOKEN no github.
8. Adicione no github à variável CLIENT `aws`.

# Instruções para configuração de input/output em nuvem

Para esse serviço usaremos o _software_ rclone, tanto para Google Drive quanto para Amazon S3.

## Google Drive

Execute "python3 get_google_token.py" em sua máquina local e siga as instruções.

## Amazon S3 

Para uso de input/output, acesse o cluster e execute o comando "rclone config" e forneça as seguintes informações quando solicitado:

```
n/s/q> n
name> nome
Storage> 4
provider> 1
env_auth> 1
access_key_id> instruções "Requisitos para Amazon S3" no README.md
secret_access_key> instruções "Requisitos para Amazon S3" no README.md
region> 16
endpoint> deixe em branco
location_constraint> 16
acl> deixe em branco
server_side_encryption> deixe em branco
sse_kms_key_id> deixe em branco
storage_class> deixe em branco
y/n> deixe em branco
y/e/d> deixe em branco
e/n/d/r/c/s/q> q
```