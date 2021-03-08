Para compilar na sua maquina siga as instruções:
**********************************************************************
- Primeiro deve ser instalado as bibliotecas do projeto:
- opencv

use o comando pip install -r requirements.txt para instalar as
demais bibliotecas.
**********************************************************************
- Segundo, no diretório do arquivo manage.py execute esses comandos:

python3 manage.py makemigrations
python3 manage.py migrate
**********************************************************************
- Terceiro, inicializer o servidor com o comando: 

python3 manage.py runserver
**********************************************************************
- Quarto, acessando as urls:
no seu browser

http://127.0.0.1:8000/upload/imagens/

Nessa url você pode realizar os uploads da imagens.
OBS: Os campos ImageAnswer e Action , estão apenas de "enfeite", não
precisando serem preenchidos.

Para obter a resposta acesser: 

http://127.0.0.1:8000/upload/imagens/answer/
**********************************************************************