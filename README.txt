# Fantasticoteca

## Descrição

Fantasticoteca é uma aplicação web desenvolvida em Django para gerenciamento e exibição de uma galeria de fotos, com autenticação de usuários, painel administrativo, busca, categorização e upload de imagens. O projeto suporta persistência de dados local (SQLite) e pode ser facilmente configurado para armazenar arquivos de mídia na AWS S3.

---

## Estrutura do Projeto

```
Fantasticoteca/
├── galeria/           # App principal da galeria de fotos
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── usuarios/          # App de autenticação de usuários
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── Fantasticoteca/    # Configurações do projeto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/             # Imagens enviadas (local)
├── static/            # Arquivos estáticos (CSS, JS, imagens)
├── templates/         # Templates HTML
│   ├── galeria/
│   └── usuarios/
├── db.sqlite3         # Banco de dados local
├── requirements.txt   # Dependências do projeto
├── manage.py
└── .env               # Variáveis de ambiente
```

---

## Funcionalidades

- Cadastro e autenticação de usuários
- Upload, visualização e categorização de fotos
- Busca por nome e categoria
- Painel administrativo Django para gerenciamento
- Layout responsivo
- Suporte a armazenamento local e AWS S3 para arquivos de mídia

---

## Instalação e Execução

1. **Clone o repositório:**
   ```sh
   git clone <url-do-repositorio>
   cd Fantasticoteca
   ```

2. **Crie e ative um ambiente virtual:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente em `.env`:**
   ```
   SECRET_KEY=SuaSecretKeyAqui
   DEBUG=True
   # Para AWS S3 (opcional)
   AWS_ACCESS_KEY_ID=SuaAWSAccessKey
   AWS_SECRET_ACCESS_KEY=SuaAWSSecretKey
   AWS_STORAGE_BUCKET_NAME=SeuBucket
   ```

5. **Execute as migrações:**
   ```sh
   python manage.py migrate
   ```

6. **Crie um superusuário:**
   ```sh
   python manage.py createsuperuser
   ```

7. **Inicie o servidor:**
   ```sh
   python manage.py runserver
   ```

8. **Observação:**
   
   Para persistência local dos dados se atentar a linha 120 do arquivo settings.py, onde haverão linhas que devem ser descomentadas.

---

## Persistência de Dados na AWS

Para armazenar arquivos de mídia (imagens) na AWS S3:

1. Instale os pacotes de integração:
   ```sh
   pip install django-storages
   ```
   ```sh
   pip install boto3
   ```

2. No `settings.py`, adicione:
   ```python
   # ...cógigo existente...
   INSTALLED_APPS += ['storages']

   if not DEBUG:
       DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
       AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
       AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
       AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
       AWS_S3_REGION_NAME = 'us-east-1'  # ajuste conforme necessário
   # ...resto do código...
   ```

3. Certifique-se de definir as variáveis no `.env` conforme o exemplo acima.

---

## Uso

- Acesse `http://localhost:8000/` para visualizar a galeria.
- Acesse `/admin/` para o painel administrativo.
- Cadastre-se ou faça login para acessar funcionalidades restritas.

---

## Principais Dependências

- Django
- python-dotenv
- django-storages (opcional, para AWS)
- boto3 (opcional, para AWS)
- Bootstrap (via CDN nos templates)

---

## Licença

Projeto educacional, sem fins comerciais.