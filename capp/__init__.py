from flask import Flask

application = Flask(__name__)

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.aboutus.routes import aboutus


application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(aboutus)