from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
	username = StringField('Username: ', validators=[DataRequired()])
	password = PasswordField('Password: ', validators=[DataRequired()])
	submit = SubmitField('Login!', validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
	username = StringField('Username: ', validators=[DataRequired()])
	