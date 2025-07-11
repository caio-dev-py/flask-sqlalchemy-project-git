from flask import Flask
from models import db, mail
from config import Config
from routes.home import home_route
from routes.form_user import form_route


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
mail.init_app(app)

app.register_blueprint(home_route)
app.register_blueprint(form_route, url_prefix='/form')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)