from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class InsertionForm(FlaskForm):
    
    week = IntegerField('Week', validators=[DataRequired()])
    deadlift = StringField('Deadlift Kg', validators=[DataRequired()])
    squat = StringField('Squat Kg', validators=[DataRequired()])
    bench_press = StringField('Bench Press Kg', validators=[DataRequired()])
    submit = SubmitField('Enter')
