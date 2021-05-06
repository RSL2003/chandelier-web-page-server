from flask_wtf import form

import forms

from forms import *
from flask import abort
from werkzeug.exceptions import Unauthorized
from flask import Flask, render_template, session, Response, request
from flask import render_template, flash, redirect, url_for
from config import Config
from flask_bootstrap import Bootstrap
import saicalls
import json

app = Flask(__name__)
app.config.from_object(Config)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
"""TODO:
1. Make the hard coded sai profile upload
2. make a brightness change option
3. pages more user friendly"""


# define your app routes
@app.route('/')
@app.route('/index')
def index():
    page = {'pagename': 'Start Page'}
    return render_template('/html/index.html', title='home', page=page)


# panel for accessing the main function of the lights
@app.route('/panel')
def panel():
    """
    Create the light control panel
    Control Panel for the light. 
    Shows admin the option to go into user admin panel.
    """
    # Check if user is admin
    if session['rank'] == "admin\n":
        isAdmin = True
    else:
        isAdmin = False
    return render_template('/html/panel.html', isAdmin=isAdmin)


# being able to add people to login to the web panel
@app.route('/userAdmin', methods=['GET', 'POST'])
def userAdmin():
    """
    User administration panel for admins to see existing users and create new ones
    """
    # yuval forgot to add a check
    if session['rank'] == "admin\n":
        # Create a list of all existing users to display to admin
        users = open('users.txt', 'r')
        lines = users.readlines()
        list_of_users = []
        for line in lines:
            username, password, rank = line.split(".")
            list_of_users.append({"username": username,
                                  "password": password,
                                  "rank": rank
                                  })
        UserForm = NewUser()
        if UserForm.validate_on_submit():
            username = UserForm.username.data
            password = UserForm.password.data
            rank = UserForm.Rank.data
            newUserString = f'{username}.{password}.{rank}\n'
            # Open a connection to users.txt
            file = open('users.txt', 'a')
            file.write(newUserString)

        return render_template('/html/userAdmin.html', users=list_of_users, form=UserForm)
    else:
        abort(401)


# Custom error codes
# noinspection PyUnusedLocal
@app.errorhandler(401)
def custom_401(error):
    return render_template('/html/error401.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Compare user inputted data to a text file with all users. 
    If not found send user back to index page. 
    If found send user to panel page. 
    Save username and rank into a session.
    """
    # Open the user file to read from 
    user_file = open('users.txt', 'r')
    lines = user_file.readlines()
    page = {'pagename': 'login'}
    # noinspection PyShadowingNames
    form = LoginForm()
    if form.validate_on_submit():
        # Save the data as a local variable
        username = form.username.data
        password = form.password.data
        # Loop through every line in the users file and find if the user exists or not
        for line in lines:
            saved_username, saved_password, saved_rank = line.split(".")
            if username == saved_username and password == saved_password:
                # Save the rank and username of the user into a session item
                session['rank'] = saved_rank
                session['username'] = username
                return redirect(url_for('panel'))
            else:
                # If user is not found
                continue
        # If user doesn't input true values send him back to the index page
        return redirect(url_for('index'))

    return render_template('/html/login.html', title='Login', page=page, form=form)


# noinspection PyUnusedLocal
@app.errorhandler(404)
def not_found_error(error):
    return render_template('/html/404.html'), 404


# noinspection PyShadowingNames,SpellCheckingInspection
@app.route('/options', methods=['GET', 'POST'])
def options():
    options = []
    with open("templates/jsonsaiprofiles/profiles.json") as f:
        data = json.load(f)
    lengthOfdata = len(data["users"])
    print(lengthOfdata)
    for i in range(lengthOfdata):
        options.append(data["profiles"][i]["name"])
    select = request.args.get('options')
    print(select)
    return render_template('/html/options.html', options=options)


@app.route('/test')  # temp testing site to ensure redirects and stuff like that
def test():
    saicalls.reset()
    return render_template('/html/test.html')


if __name__ == '__main__':
    app.run(debug=True)
    FLASK_DEBUG = 1
