from forms import LoginForm
from flask import Flask, render_template
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


@app.route('/login', methods=['GET', 'POST'])
def login():
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
                # If user is found
                list = []
                list.append(saved_rank)
                print(list)
                if (saved_rank=="admin\n"):
                    print("here1")
                    new_username = saved_username
                    return render_template('/html/panel.html', name=saved_username)
                if (saved_rank=="user"):
                    return render_template('/html/panel.html', name=saved_username)
            else:
                # If user is not found
                continue
        
    return render_template('/html/login.html', title='Login', page=page, form=form)


if __name__ == '__main__':
    app.run(debug=True)
