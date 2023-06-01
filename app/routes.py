from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template('index.html', name='Favorite places')


@app.route("/favorite")
def favorite():
    favorite = [
        ('image'),
        ('image'),
        ('image'),
        ('image'),
        ('image')
    ]
    return render_template('favorites.html' )