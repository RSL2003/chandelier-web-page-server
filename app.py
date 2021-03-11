from forms import *
from flask import Flask, render_template, session
from flask import render_template, flash, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy  # prob wont use in final version
# from flask_migrate import Migrate  # most likely wont use in final version
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
app.config.from_object(Config)
bootstrap = Bootstrap(app)


# define your app routes
@app.route('/')
@app.route('/index')
def index():
    page = {'pagename': 'Start Page'}
    return render_template('/html/index.html', title='home', page=page)

@app.route('/panel')
def panel():
    """
    TODO:
    Create the light control panel
    Control Panel for the light. 
    Shows admin the option to go into user admin panel.
    """
    # Check if user is admin
    if (session['rank'] == "admin\n"):
        isAdmin = True
    else:
        isAdmin = False
    return render_template('/html/panel.html', isAdmin=isAdmin)

@app.route('/userAdmin', methods=['GET', 'POST'])
def userAdmin():
    """
    User administration panel for admins to see existing users and create new ones
    """
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
    form = LoginForm()
    if form.validate_on_submit():
        # Save the data as a local variable
        username = form.username.data
        password = form.password.data
        # Loop through every line in the users file and find if the user exists or not
        for line in lines:
            saved_username, saved_password, saved_rank = line.split(".")
            if (username==saved_username and password==saved_password):
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


if __name__ == '__main__':
    app.run(debug=True)
