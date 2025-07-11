import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

class Config:
    # configurações app
    SECRET_KEY = os.getenv('SECRET_KEY')

    # configurações sqlalchemy
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, 'database.db')}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # configurações envio de e-mail

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')

