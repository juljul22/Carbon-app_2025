from flask import Flask
from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app

application = Flask(__name__)

# Blueprints registrieren
application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
