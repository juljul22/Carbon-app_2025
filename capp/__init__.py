from flask import Flask

application = Flask(__name__)

from capp.home.routes import home
from capp.calculator.routes import calculator
from capp.aboutus.routes import aboutus

application.register_blueprint(home)
application.register_blueprint(calculator)
application.register_blueprint(aboutus)
