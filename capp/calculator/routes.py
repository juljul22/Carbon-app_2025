from flask import render_template, Blueprint, request, redirect, url_for, flash
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.calculator.forms import BusForm, CarForm, PlaneForm, FerryForm, TrainForm, WalkForm

calculator=Blueprint('calculator',__name__)

#Emissions factor per transport in kg per passemger km
#Data from: http://efdb.apps.eea.europa.eu/?source=%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%2C%22display_type%22%3A%22tabular%22%7D
efco2={'Bus':{'Diesel':0.10231},
    'Car':{'Petrol':0.18592,'Diesel':0.16453,'Electric':0},
    'Plane':{'Economy':0.24298,'Business':0.222},
    'Ferry':{'Diesel':0.11131, 'CNG':0.1131, 'No Fossil Fuel':0},
    'Train':{'Diesel':0.09816,'Electric':0},
    'Walk':{'No Fossil Fuel':0}}



#Carbon app, main page
@calculator.route('/calculator')
@login_required
def calculator_home():
  return render_template('calculator/calculator_home.html', title='calculator')


#Carbon app, car
@calculator.route('/calculator/new_entry_car')
@login_required
def new_entry_car():
    return render_template('calculator/new_entry_car.html', title='Car Calculator')

#Carbon app, plane
@calculator.route('/calculator/new_entry_plane')
@login_required
def new_entry_plane():
    return render_template('calculator/new_entry_plane.html', title='Plane Calculator')

#Carbon app, walk
@calculator.route('/calculator/new_entry_walk')
@login_required
def new_entry_walk():
    return render_template('calculator/new_entry_walk.html', title='Walk Calculator')


#Carbon app, bus
@calculator.route('/calculator/new_entry_bus', methods=['GET', 'POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'

        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))

        emissions = Transport(
            kms=kms,
            transport=transport,
            fuel=fuel,
            co2=co2,
            author=current_user
        )
        db.session.add(emissions)
        db.session.commit()

        return redirect(url_for('calculator.your_data'))

    return render_template(
        'calculator/new_entry_bus.html',
        title='Bus Calculator',
        form=form
    )

#Carbon app, ferrry
@calculator.route('/calculator/new_entry_ferry')
@login_required
def new_entry_ferry():
    return render_template('calculator/new_entry_ferry.html', title='Ferry Calculator')

#Carbon app, train
@calculator.route('/calculator/new_entry_train')
@login_required
def new_entry_train():
    return render_template('calculator/new_entry_train.html', title='Train Calculator')


#Your data
@calculator.route('/calculator/your_data')
@login_required

def your_data():
    #Table
    entries = Transport.query.filter_by(author=current_user). \
        filter(Transport.date> (datetime.now() - timedelta(days=5))).\
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()
    return render_template('calculator/your_data.html', title='your_data', entries=entries)

    #Delete emission
@calculator.route('/calculator/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('calculator.your_data'))