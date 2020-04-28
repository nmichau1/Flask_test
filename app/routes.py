from flask import render_template
from app import app
from model_joins import Coordinates
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    Coordinates = Coordinates

    posts = [
        {

            'author' : {'username': 'John'},
            'body' : 'Beautiful day in Portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title = 'Home', user=user, posts= posts, Coordinates = Coordinates)