# Sistema de Controle de Férias - Django

## 🐳 Execução com Docker (Recomendado)

### Pré-requisitos
- Docker Desktop instalado
- Docker Compose

### Passos para executar:

1. **Clone o repositório ou navegue até a pasta:**
```bash
cd django_ferias
```

2. **Construir e iniciar os containers:**
```bash
docker-compose up --build
```

3. **Acessar a aplicação:**
- Sistema: http://localhost:8000/
- Admin: http://localhost:8000/admin/

4. **Criar superusuário (em outro terminal):**
```bash
docker-compose exec web python manage.py createsuperuser
```

5. **Parar os containers:**
```bash
docker-compose down
```

6. **Parar e remover volumes (dados do banco):**
```bash
docker-compose down -v
```

### Comandos úteis:

```bash
# Ver logs
docker-compose logs -f

# Executar comandos Django
docker-compose exec web python manage.py <comando>

# Acessar shell do Django
docker-compose exec web python manage.py shell

# Fazer migrations
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

# Coletar arquivos estáticos
docker-compose exec web python manage.py collectstatic --no-input
```

---

## 💻 Instalação Manual (Sem Docker)

### Requisitos
- Python 3.8+
- MySQL 5.7+
- pip

## Instalação

1. **Criar ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

3. **Configurar MySQL:**
```sql
CREATE DATABASE ferias_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

4. **Configurar settings.py:**
Edite `ferias_project/settings.py` e ajuste as credenciais do MySQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ferias_db',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. **Criar estrutura do projeto:**
```bash
django-admin startproject ferias_project .
python manage.py startapp ferias
```

6. **Aplicar migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Criar superusuário:**
```bash
python manage.py createsuperuser
```

8. **Executar servidor:**
```bash
python manage.py runserver
```

9. **Acessar:**
- Sistema: http://localhost:8000/
- Admin: http://localhost:8000/admin/

## Funcionalidades

- ✅ Cadastrar férias
- ✅ Listar férias com filtros
- ✅ Editar férias
- ✅ Excluir férias
- ✅ Visualizar detalhes
- ✅ Estatísticas
- ✅ Interface responsiva com Bootstrap 5

## Estrutura do Projeto

```
django_ferias/
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env.example
├── ferias_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── ferias/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── templates/
│   ├── base.html
│   └── ferias/
│       ├── listar.html
│       ├── form.html
│       ├── visualizar.html
│       └── confirmar_delete.html
├── requirements.txt
└── README.md
```

## 🔧 Variáveis de Ambiente

Crie um arquivo `.env` baseado no `.env.example`:

```bash
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
ALLOWED_HOSTS=localhost,127.0.0.1

DB_HOST=db
DB_PORT=3306
DB_NAME=ferias_db
DB_USER=ferias_user
DB_PASSWORD=ferias_password
```

## 🚀 Produção

Para ambiente de produção, considere:

1. Mudar `DEBUG=False`
2. Configurar `SECRET_KEY` segura
3. Definir `ALLOWED_HOSTS` apropriadamente
4. Usar servidor WSGI (Gunicorn)
5. Configurar servidor web (Nginx)
6. Configurar SSL/HTTPS
7. Usar variáveis de ambiente para senhas
8. Fazer backup regular do banco de dados
