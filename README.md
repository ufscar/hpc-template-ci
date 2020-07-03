# Template Integração Contínua Github

Esse projeto o template para uso do cluster da UFSCar, contendo integração contínua com o Google Drive e AWS S3.

## Requisitos para Google Drive

1. Entre no [console de credenciais de API do Google](https://console.developers.google.com/apis/credentials)
2. Clique em "Criar credenciais".
3. Selecione "ID do cliente do OAuth".
4. Em "Tipo de aplicativo", selecione "App para computador".
5. Dê um nome de identificação para as credenciais e clique em "criar".
6. Clique em "OK".
7. Clique no último botão na linha da credencial criada (seta para baixo) e salve o arquivo em um local seguro.
8. No computador, copie o arquivo para ~/.secrets/.google/.credentials (arquivo com nome .credentials).
9. Execute o script `python3 get_google_token.py`.
10. Adicione o conteúdo indicado na saída na variável de ambiente CREDENTIALS_GOOGLE no github (projeto >> Settings >> Secrets >> New Secret).
11. Adicione no github à variável COLLECTION_CONTAINER `/path/to/project`, esse será o caminho cujo container vai ser disponibilizado no seu Google Drive no formato `recipe_nameDateTime.simg`.
12. Acessar o site da [Sylabs Cloud](cloud.sylabs.io), criar um _access token_, copiar e adicionar na variável SYLABS_TOKEN no github.
13. Adicione no github à variável CLIENT `google`.


## Requisitos para Amazon S3

1. Entre na [AWS](console.aws.amazon.com)
2. Clique na seta ao lado de seu nome de usuário e em "My Security Credentials".
3. Na seção "Access Keys", clique em "Create New Access Key".
4. Na janela que aparece, clique em "Show Access Key".
5. Copie o conteúdo de "Access Key ID" na variável ACCESS_KEY_AWS no github (projeto >> Settings >> Secrets >> New Secret).
6. Copie o conteúdo de "Secret Access Key" na variável SECRET_KEY_AWS no github.
7. Acessar o site da [Sylabs Cloud](cloud.sylabs.io), criar um _access token_, copiar e adicionar na variável SYLABS_TOKEN no github.
8. Adicione no github à variável CLIENT `aws`.