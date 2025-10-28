from flask import Flask, render_template, url_for
application = Flask(__name__)

@application.route('/')
@application.route('/home')
def home():
    return render_template('home.html')

@application.route('/methodology')
def methodology():
    return render_template('methodology.html')

if __name__=='__main__':
    application.run(debug=True)  
