from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'be71c7b26d91bab789949265204785b6'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # importar e registrar blueprints
    from app.routes.auth import auth
    from app.routes.main import main
    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app