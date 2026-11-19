# Sistema de Clínica Médica

## 1. Sobre o projeto

Este projeto consiste no desenvolvimento de um sistema web para gerenciamento de uma clínica médica.

A aplicação utiliza Django como framework backend, MySQL como banco de dados e Docker para configuração e execução do ambiente de desenvolvimento.

Atualmente, o projeto possui a estrutura inicial do sistema, com configuração do ambiente, conexão com o banco de dados, organização dos arquivos estáticos e criação das primeiras páginas da aplicação.

## 2. Tecnologias utilizadas

- Python 3.12
- Django
- MySQL 8.4
- Docker
- Docker Compose
- HTML5
- CSS3

## 3. Estrutura do projeto

```text
clinica/
│
├── backend/
│   │
│   ├── clinica/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   │
│   ├── core/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── img/
│   │   └── js/
│   │
│   ├── templates/
│   │   ├── home.html
│   │   └── login_medico.html
│   │
│   └── manage.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── LICENSE
├── README.md
└── venv/
```

## 4. Backend Django

O backend está localizado no diretório `backend/`.

A aplicação Django está organizada em dois módulos principais:

### clinica

Responsável pelas funcionalidades relacionadas ao sistema da clínica.

Arquivos principais:

- views.py: contém as funções responsáveis por processar as requisições e renderizar as páginas.
- models.py: destinado à definição dos modelos e estruturas de dados.
- admin.py: configuração do painel administrativo.
- migrations/: armazenamento das migrações do banco de dados.
- tests.py: destinado aos testes automatizados.

### core

Contém as configurações principais do projeto Django.

Arquivos principais:

- settings.py: configurações gerais, aplicativos instalados, banco de dados, templates e arquivos estáticos.
- urls.py: definição das rotas da aplicação.
- asgi.py: configuração da interface ASGI.
- wsgi.py: configuração da interface WSGI.

## 5. Rotas disponíveis

As rotas são configuradas em `backend/core/urls.py` e utilizam as funções definidas em `backend/clinica/views.py`.

Atualmente, estão disponíveis:

| Rota | View | Template |
|---|---|---|
| / | home | home.html |
| /login | login_medico | login_medico.html |
| /admin/ | Administração Django | Painel administrativo |

### Página inicial

A rota `/` executa a função `home`, responsável por renderizar o template `home.html`.

### Login do médico

A rota `/login` executa a função `login_medico`, responsável por renderizar o template `login_medico.html`.

Observação: a página de login está criada, mas a implementação da autenticação ainda não está documentada como funcionalidade concluída.

## 6. Templates e arquivos estáticos

Os templates HTML estão armazenados em:

`backend/templates/`

Arquivos existentes:

- home.html
- login_medico.html

Os arquivos estáticos estão organizados em:

`backend/static/`

Diretórios disponíveis:

- css/: folhas de estilo.
- img/: imagens.
- js/: arquivos JavaScript.

A folha de estilos compartilhada está localizada em:

`backend/static/css/style.css`

O Django utiliza a configuração `STATICFILES_DIRS` para localizar os arquivos estáticos durante o desenvolvimento.

Os templates utilizam a tag `{% load static %}` para carregar os arquivos CSS.

Exemplo:

`{% static 'css/style.css' %}`

## 7. Banco de dados MySQL

O projeto utiliza MySQL 8.4 como sistema de gerenciamento de banco de dados.

O banco é executado em um container Docker separado da aplicação Django.

Configurações atuais do ambiente:

- Banco de dados: clinic
- Usuário: clinic
- Host utilizado pelo Django: db
- Porta: 3306

A comunicação entre Django e MySQL ocorre por meio da rede interna criada pelo Docker Compose.

### Persistência dos dados

O Docker Compose utiliza um volume nomeado:

`mysql_data`

Esse volume armazena os dados do MySQL em `/var/lib/mysql`, permitindo que os dados persistam mesmo quando os containers são removidos.

## 8. Docker e Docker Compose

O projeto utiliza Docker para padronizar o ambiente de desenvolvimento e facilitar a execução da aplicação.

### Dockerfile

O Dockerfile utiliza a imagem `python:3.12-slim`.

Durante a construção da imagem, são realizadas as seguintes etapas:

1. Definição do diretório de trabalho `/app`.
2. Instalação das dependências necessárias para compilar e conectar o driver MySQL.
3. Cópia do arquivo `requirements.txt`.
4. Instalação das dependências Python.
5. Cópia dos arquivos do projeto para o container.
6. Definição do comando de inicialização do Django.

### Docker Compose

O arquivo `docker-compose.yml` define dois serviços:

**db**

Responsável pela execução do MySQL 8.4.

Possui configuração de healthcheck para verificar se o banco está pronto para receber conexões.

**web**

Responsável pela execução da aplicação Django.

O serviço realiza automaticamente as migrações do banco de dados e inicia o servidor de desenvolvimento na porta 8000.

Também utiliza um volume de montagem do diretório do projeto para facilitar o desenvolvimento sem precisar reconstruir a imagem a cada alteração nos arquivos.

## 9. Como executar o projeto

### Pré-requisitos

É necessário possuir:

- Docker instalado.
- Docker Compose disponível pelo comando `docker compose`.
- Git instalado, caso o projeto seja obtido por meio de um repositório.

### Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
cd clinica
```

### Iniciar a aplicação

Para construir a imagem e iniciar os containers:

```bash
docker compose up --build
```

Para executar os containers em segundo plano:

```bash
docker compose up -d
```

### Acessar a aplicação

Após a inicialização, a aplicação estará disponível em:

Página inicial:
http://localhost:8000/

Login do médico:
http://localhost:8000/login

Painel administrativo:
http://localhost:8000/admin/

### Verificar os containers

```bash
docker compose ps
```

### Visualizar os logs

```bash
docker compose logs -f
```

Para visualizar somente os logs da aplicação Django:

```bash
docker compose logs -f web
```

### Executar comandos Django

Criar migrações:

```bash
docker compose exec web python backend/manage.py makemigrations
```

Aplicar migrações:

```bash
docker compose exec web python backend/manage.py migrate
```

Criar um superusuário:

```bash
docker compose exec web python backend/manage.py createsuperuser
```

Abrir o shell interativo do Django:

```bash
docker compose exec web python backend/manage.py shell
```

### Parar os containers

```bash
docker compose stop
```

### Iniciar containers já existentes

```bash
docker compose start
```

### Encerrar e remover os containers

```bash
docker compose down
```

Observação: o comando `docker compose down` não remove o volume nomeado do MySQL. Para preservar os dados, evite utilizar `docker compose down -v`, pois essa opção também remove os volumes.

## 10. Configurações e segurança

As configurações do Django e do banco de dados são fornecidas por variáveis de ambiente.

O projeto utiliza `python-decouple` para leitura das configurações no arquivo `settings.py`.

Para ambientes de produção, recomenda-se:

- Utilizar um arquivo `.env` para armazenar variáveis sensíveis.
- Não publicar senhas, chaves secretas ou credenciais no repositório.
- Configurar `DEBUG=False`.
- Definir os hosts permitidos em `ALLOWED_HOSTS`.
- Utilizar senhas fortes para o banco de dados.
- Configurar um servidor de aplicação adequado para produção, em vez do servidor de desenvolvimento do Django.

As credenciais atualmente definidas no Docker Compose são destinadas ao ambiente de desenvolvimento e devem ser substituídas por configurações seguras antes da implantação.

## 11. Estado atual do desenvolvimento

Até o momento, foram realizadas as seguintes implementações:

- Configuração inicial do projeto Django.
- Configuração do banco de dados MySQL.
- Containerização da aplicação com Docker.
- Configuração do Docker Compose.
- Configuração da persistência dos dados do MySQL.
- Organização da