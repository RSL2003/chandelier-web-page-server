from forms import LoginForm
from flask import Flask, render_template
from flask import render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy  # prob wont use in final version
from flask_migrate import Migrate  # most likely wont use in final version
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
    page = {'pagename': 'login'}
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('/html/login.html', title='Login', page=page, form=form)


if __name__ == '__main__':
    app.run(debug=True)
