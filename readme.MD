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
- [Documentação Flask](https://flask.palletsprojects.com/)

- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)

- [Bootstrap 5](https://getbootstrap.com/)

- [Jinja2 Templates](https://jinja.palletsprojects.com/)

```
🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. 