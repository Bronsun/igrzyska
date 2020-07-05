from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError


class DudaForm(FlaskForm):
    answer = TextAreaField('Odpowiedz',validators=[DataRequired()])
    submit = SubmitField('Wyślij odpowiedź')

class TrzaskForm(FlaskForm):
    answer = TextAreaField('Odpowiedz',validators=[DataRequired()])
    submit = SubmitField('Wyślij odpowiedź')