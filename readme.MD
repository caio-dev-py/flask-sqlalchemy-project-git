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


---

## ⚙️ Como Rodar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd flask-sqlalchemy-project
