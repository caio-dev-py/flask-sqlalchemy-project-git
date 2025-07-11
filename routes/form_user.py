from flask import Blueprint, render_template, url_for, redirect, flash, request 
from models import db, usuario, nota
from functions import validar_email

form_route = Blueprint('form', __name__)

@form_route.route('/')
def form():  
    return render_template('form_user.html')

@form_route.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    nome = request.form.get('nome')
    email = request.form.get('email')
    nota_mensagem = request.form.get('nota')

    if not nome:
        flash('Preencha o nome.', 'danger')
    
    if not validar_email(email):
        flash('E-mail inválido. Preencha com um e-mail válido.', 'danger')
    
    if not nota_mensagem:
        flash('Escreva alguma mensagem.', 'danger')

    if request.method == 'POST':
        
        email_existente = usuario.query.filter_by(email=email).first()
        if not email_existente:
            dados_usuario = usuario(nome=nome, email=email)
            db.session.add(dados_usuario)
            db.session.commit()
        
            nota_existente = nota.query.filter_by(nota=nota_mensagem).first()
            if not nota_existente:
                dados_nota = nota(nota=nota_mensagem, usuario_id=dados_usuario.id)
                db.session.add(dados_nota)
                db.session.commit()

                nome_existente = usuario.query.filter_by(nome=nome).first()
                if not nome_existente:
                    flash ('Os dados foram enviados com sucesso.', 'success')
        
        return redirect(url_for('form.form'))
    
    flash('Dados enviados.', 'success')
    return render_template('form_user.html', nome=nome, email=email)

@form_route.route('/atualizar_usuario')
def atualizar_usuario():
    pass

@form_route.route('/remover_usuario')
def remover_usuario():
    pass