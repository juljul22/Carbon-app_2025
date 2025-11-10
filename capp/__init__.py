from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


# Create the Flask app
application = Flask(__name__)
application.secret_key = "une_cle_ultra_secrete_a_changer"

# Database configuration
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
application.config['SQLALCHEMY_BINDS'] = {'transport': 'sqlite:///transport.db'}
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database + bcrypt
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)

# Import Blueprints
from capp.home.routes import home
from capp.calculator.routes import calculator
from capp.aboutus.routes import aboutus
from capp.users.routes import users

# Register Blueprints
application.register_blueprint(home)
application.register_blueprint(calculator)
application.register_blueprint(aboutus)
application.register_blueprint(users)
