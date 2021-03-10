from forms import LoginForm # issues with this import still
from flask import Flask, render_template


from config import Config

app = Flask(__name__)
app.config.from_object(Config)


# define your app routes
@app.route('/')
@app.route('/index')
def index():
    page = {'pagename': 'Start Page'}
    return render_template('index.html', title='home', page=page)


@app.route('/login')   # still has issues with loading
def login():
    page = {'pagename': 'login'}
    form = LoginForm
    return render_template('login.html', title='Login', page=page, form=form)


if __name__ == '__main__':
    app.run(debug=True)
