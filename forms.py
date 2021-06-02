from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired
import json



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class testform(FlaskForm):
    number = StringField('Type a number', validators=[DataRequired()])
    submit = SubmitField('Submit Number')


class NewUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    myChoices = 2
    Rank = SelectField(u'Permissions', choices = ['admin', 'user'], validators=[DataRequired()])
    submit = SubmitField('Sign In')

class chooseProfile(FlaskForm):
    options = [ ]
    with open("SAI_PROFILES.json") as f:
        data = json.load(f)
    #  forms.chooseProfile()
    lengthOfdata = len(data)
    # print(lengthOfdata)
    options = data.keys()
    profileName = SelectField('Profile', choices=options, validators=[DataRequired()])
    submit = SubmitField('submit')

class trigger(FlaskForm):
    submit = SubmitField('Trigger')