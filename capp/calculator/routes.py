from flask import render_template, Blueprint

calculator=Blueprint('calculator',__name__)

@calculator.route('/calculator')
def calculator_home():
  return render_template('calculator.html', title='calculator')