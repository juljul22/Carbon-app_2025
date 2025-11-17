from flask_wtf import FlaskForm
from wtforms import  SubmitField,  SelectField,  FloatField
from wtforms.validators import InputRequired

class BusForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
  choices=[('Diesel', 'Diesel')])
  submit = SubmitField('Submit')

class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
  choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric')])
  submit = SubmitField('Submit')  

class PlaneForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()]), 
  choices=[('Economy', 'Economy'), ('Business', 'Business')]
  submit = SubmitField('Submit')
  
class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
  choices=[('Diesel', 'Diesel'), ('CNG', 'CNG'), ('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

class TrainForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('Electric', 'Electric')])
  submit = SubmitField('Submit')

class WalkForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  