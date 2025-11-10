from flask import render_template, Blueprint

calculator=Blueprint('calculator',__name__)


#Carbon app, main page
@calculator.route('/calculator')
def calculator_home():
  return render_template('calculator/calculator_home.html', title='calculator')


#Carbon app, car
@calculator.route('/calculator/new_entry_car')
def new_entry_car():
    return render_template('calculator/new_entry_car.html', title='Car Calculator')

#Carbon app, plane
@calculator.route('/calculator/new_entry_plane')
def new_entry_plane():
    return render_template('calculator/new_entry_plane.html', title='Plane Calculator')

#Carbon app, walk
@calculator.route('/calculator/new_entry_walk')
def new_entry_walk():
    return render_template('calculator/new_entry_walk.html', title='Walk Calculator')

#Carbon app, bus
@calculator.route('/calculator/new_entry_bus')
def new_entry_bus():
    return render_template('calculator/new_entry_bus.html', title='Bus Calculator')

#Carbon app, ferrry
@calculator.route('/calculator/new_entry_ferry')
def new_entry_ferry():
    return render_template('calculator/new_entry_ferry.html', title='Ferry Calculator')

#Carbon app, train
@calculator.route('/calculator/new_entry_train')
def new_entry_train():
    return render_template('calculator/new_entry_train.html', title='Train Calculator')
