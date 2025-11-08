from flask import render_template, Blueprint

calculator=Blueprint('calculator',__name__)


#Carbon app, main page
@calculator.route('/calculator')
def calculator_home():
  return render_template('calculator/calculator_home.html', title='calculator')