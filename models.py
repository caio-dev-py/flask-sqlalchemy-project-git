from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime

mail = Mail()
db = SQLAlchemy()

class usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    nome = db.Column(db.String(150), nullable=False)
    nota = db.relationship('nota', backref='usuario', lazy=True)
    
class nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.String(10000))
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    date = db.Column(db.DateTime, default=datetime.utcnow)