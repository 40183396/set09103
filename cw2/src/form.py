from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(Form):
    username = TextField(
            'username',
            validators=[DataRequired(), Length(min=3, max=30)]
    )
    email = TextField(
        'email',
         validators=[DataRequired(),Email(message=None), Length(min=3, max=30)]
    )
    password = PasswordField(
        'password',
        validators=[DataRequired(),Length(min=6, max=30)]
    )
    confirm = PasswordField(
          'Repeat password',
          validators=[
              DataRequired(),EqualTo('password',message='Passwords should be the same.')
          ]
    )
