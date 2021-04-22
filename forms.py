from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class NewUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    myChoices = 2
    Rank = SelectField(u'Permissions', choices = ['admin', 'user'], validators=[DataRequired()])
    submit = SubmitField('Sign In')

class chooseProfile(FlaskForm):
    profileName = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('submit')


class jsonprofileeditor(FlaskForm):
    print('hello world')
