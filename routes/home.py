from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template('home.html')

@home_route.route('/servicos')
def sobre():
    return render_template('servicos.html')