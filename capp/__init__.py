from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

# application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  
application.config['SECRET_KEY'] = '3oueqkfdfas8ruewqndr8ewrewrouewrere44554'

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
application.config['SQLALCHEMY_BINDS'] ={'transport': 'sqlite:///transport.db'}


db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from capp.home.routes import home
from capp.calculator.routes import calculator
from capp.aboutus.routes import aboutus
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(calculator)
application.register_blueprint(aboutus)
application.register_blueprint(users)