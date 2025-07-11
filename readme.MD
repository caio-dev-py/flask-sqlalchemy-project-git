# 📦 Flask-SQLAlchemy Project

Um projeto de aprendizado usando **Python + Flask**, com integração ao **Flask-SQLAlchemy**, **HTML/CSS**, **Bootstrap**, e várias funções úteis do Flask como `flash()`, `redirect()`, `url_for()`, `Blueprints`, entre outras.

---

## 🚀 Objetivo

Este projeto tem como objetivo praticar e consolidar conhecimentos em:
- Flask (framework web em Python)
- Flask-SQLAlchemy (ORM para banco de dados)
- HTML, CSS e **Bootstrap 5**
- Estrutura de rotas e Blueprints
- Validação de formulários e e-mails
- Mensagens flash
- Templates dinâmicos com Jinja2

---

## 🧠 Tecnologias Usadas

| Tecnologia        | Descrição                                       |
|-------------------|-------------------------------------------------|
| Python            | Linguagem principal                             |
| Flask             | Framework web leve                              |
| Flask-SQLAlchemy  | ORM para interagir com banco de dados SQLite    |
| HTML & CSS        | Interface do usuário                            |
| Bootstrap 5       | Framework CSS responsivo e moderno              |
| Jinja2            | Templates dinâmicos (ex: `{{ variavel }}`)      |
| Flash             | Exibir mensagens rápidas para o usuário         |

---

## 📁 Estrutura do Projeto
```
flask-sqlalchemy-project/
│
├── static/ # Arquivos estáticos (CSS, JS, imagens, Bootstrap)
├── templates/ # Templates HTML com Jinja2 e Bootstrap
├── routes/ # Blueprints e rotas separadas
├── config.py # Configuração da aplicação Flask
├── main.py # Arquivo principal para rodar o app
├── models.py # Modelos SQLAlchemy (Tabelas)
├── functions.py # Funções auxiliares (ex: validação de email)
├── database.db # Banco de dados SQLite
├── .env # Variáveis de ambiente (ex: SECRET_KEY)
└── .gitignore # Arquivos ignorados pelo Git
```

---

## ⚙️ Como Rodar o Projeto

1. Clone o repositório:
```
bash

git clone https://github.com/seu-usuario/seu-repo.git
cd flask-sqlalchemy-project

bash

git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
Crie um ambiente virtual (opcional, mas recomendado):

bash

python -m venv venv
source venv/bin/activate  # Linux / MacOS
venv\Scripts\activate     # Windows
Instale as dependências:

bash

pip install -r requirements.txt
Configure o banco de dados (SQLite por padrão) e outras variáveis em config.py, se necessário.

Execute a aplicação:

bash

python app.py
Acesse no navegador: http://127.0.0.1:5000

🛠 Funcionalidades
Cadastro, edição e listagem de usuários e notas

Validação de dados no formulário

Mensagens flash para feedback do usuário

Interface responsiva com Bootstrap 5

Uso de Blueprints para organização das rotas

Template base para reaproveitamento de layout

Integração com banco de dados SQLite via Flask-SQLAlchemy

⚙️ Tecnologias e Bibliotecas
Flask: pip install Flask

Flask-SQLAlchemy: pip install Flask-SQLAlchemy

Bootstrap 5: Incluído via CDN no template base

Outras bibliotecas podem estar listadas no requirements.txt
```
📚 Referências e Recursos

- [Flask 3.1.1](https://flask.palletsprojects.com/en/3.1.x/) – Framework web em Python

- [Flask-SQLAlchemy 3.1.1](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/) – ORM para Flask

- [SQLAlchemy 2.0.41](https://docs.sqlalchemy.org/en/20/) – Biblioteca ORM para Python

- [Jinja2 3.1.6](https://jinja.palletsprojects.com/en/3.1.x/) – Template engine para Python

- [Werkzeug 3.1.3](https://werkzeug.palletsprojects.com/en/3.1.x/) – Biblioteca WSGI para Python, usada pelo Flask

- [click 8.2.1](https://click.palletsprojects.com/en/8.2.x/) – Biblioteca para criação de comandos de terminal

- [python-dotenv 1.1.1](https://github.com/theskumar/python-dotenv) – Lê variáveis de ambiente de arquivos .env

- [email_validator 2.2.0](https://pypi.org/project/email-validator/) – Validação de emails

- [blinker 1.9.0](https://pypi.org/project/blinker/) – Biblioteca para sinais (signals)

- [greenlet 3.2.3](https://pypi.org/project/greenlet/) – Biblioteca para programação concorrente

- [colorama 0.4.6](https://pypi.org/project/colorama/) – Coloração do terminal para Windows

- [dnspython 2.7.0](https://pypi.org/project/dnspython/) – Biblioteca para DNS

- [idna 3.10](https://pypi.org/project/idna/) – Suporte para nomes de domínio internacionalizados

- [itsdangerous 2.2.0](https://pypi.org/project/itsdangerous/) – Ferramentas para dados seguros

- [MarkupSafe 3.0.2](https://pypi.org/project/MarkupSafe/) – Segurança em strings para templates

- [typing_extensions 4.14.1](https://pypi.org/project/typing-extensions/) – Extensões para tipagem do Python

```
🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. 