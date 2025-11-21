from flask import render_template, Blueprint, request, redirect, url_for, flash
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.calculator.forms import BusForm, CarForm, PlaneForm, FerryForm, TrainForm, WalkForm
import json

calculator = Blueprint('calculator', __name__)

# Emissions factor per transport in kg per passenger km
# Data from: 
efco2 = {
    'Bus': {'Diesel': 0.030},
    'Car': {'Petrol': 0.198, 'Diesel': 0.228, 'Electric': 0.059},
    'Plane': {'Economy': 0.127, 'Business': 0.289},
    'Ferry': {'Passenger with car': 0.377, 'Passenger only': 0.186},
    'Train': {'Diesel': 0.091, 'Electric': 0.007},
    'Walk': {'No Fossil Fuel': 0}
}

# Carbon app, main page
@calculator.route('/calculator')
@login_required
def calculator_home():
    return render_template('calculator/calculator_home.html', title='calculator')

# Carbon app, plane
@calculator.route('/calculator/new_entry_plane', methods=['GET', 'POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'

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
        'calculator/new_entry_plane.html',
        title='Plane Calculator',
        form=form
    )

# Carbon app, walk
@calculator.route('/calculator/new_entry_walk', methods=['GET', 'POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Walk'

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
        'calculator/new_entry_walk.html',
        title='Walk/Bike Calculator',
        form=form
    )

# Carbon app, bus
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

# Carbon app, car
@calculator.route('/calculator/new_entry_car', methods=['GET', 'POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'

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
        'calculator/new_entry_car.html',
        title='Car Calculator',
        form=form
    )

# Carbon app, ferry
@calculator.route('/calculator/new_entry_ferry', methods=['GET', 'POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'

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
        'calculator/new_entry_ferry.html',
        title='Ferry Calculator',
        form=form
    )

# Carbon app, train
@calculator.route('/calculator/new_entry_train', methods=['GET', 'POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Train'

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
        'calculator/new_entry_train.html',
        title='Train Calculator',
        form=form
    )

# Your data
@calculator.route('/calculator/your_data')
@login_required
def your_data():
    # Table
    entries = Transport.query.filter_by(author=current_user).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).\
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()

    # Emissions by category
    emissions_by_transport = db.session.query(db.func.sum(Transport.total), Transport.transport).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        group_by(Transport.transport).order_by(Transport.transport.asc()).all()

    emission_transport = [0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in emissions_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        emission_transport[1] = first_tuple_elements[index_bus]

    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        emission_transport[2] = first_tuple_elements[index_car]

    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        emission_transport[3] = first_tuple_elements[index_ferry]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        emission_transport[4] = first_tuple_elements[index_plane]

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        emission_transport[5] = first_tuple_elements[index_train]

    if 'Walk' in second_tuple_elements:
        index_walk = second_tuple_elements.index('Walk')
        emission_transport[6] = first_tuple_elements[index_walk]

    # Kilometers by category
    kms_by_transport = db.session.query(db.func.sum(Transport.kms), Transport.transport).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        group_by(Transport.transport).order_by(Transport.transport.asc()).all()

    kms_transport = [0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in kms_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        kms_transport[1] = first_tuple_elements[index_bus]

    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        kms_transport[2] = first_tuple_elements[index_car]

    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        kms_transport[3] = first_tuple_elements[index_ferry]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        kms_transport[4] = first_tuple_elements[index_plane]

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        kms_transport[5] = first_tuple_elements[index_train]

    if 'Walk' in second_tuple_elements:
        index_walk = second_tuple_elements.index('Walk')
        kms_transport[6] = first_tuple_elements[index_walk]

    # Emissions by date (individual)
    emissions_by_date = db.session.query(db.func.sum(Transport.total), Transport.date).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        group_by(Transport.date).order_by(Transport.date.asc()).all()

    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)

    # Kms by date (individual)
    kms_by_date = db.session.query(db.func.sum(Transport.kms), Transport.date).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        group_by(Transport.date).order_by(Transport.date.asc()).all()

    over_time_kms = []
    dates_label = []
    for total, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(total)

    return render_template(
        'calculator/your_data.html',
        title='your_data',
        entries=entries,
        emissions_by_transport_python_dic=emissions_by_transport,
        emission_transport_python_list=emission_transport,
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label)
    )

# Delete emission
@calculator.route('/calculator/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('calculator.your_data'))
