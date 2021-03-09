from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    page = {'pagename': 'Start Page'}
    return render_template('index.html', title='home', page=page)


if __name__ == '__main__':
    app.run(debug=True)
