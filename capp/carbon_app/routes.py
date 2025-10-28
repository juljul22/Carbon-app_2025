from flask import render_template, Blueprint

carbon_app=Blueprint('carbon_app',__name__)

@carbon_app.route('/home')
def home():
    return render_template('home.html', title='Home')

@carbon_app.route('/methodology')
def methodology():
    return render_template('methodology.html', title='Methodology')



    
