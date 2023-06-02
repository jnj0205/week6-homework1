from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template('index.html', name='Favorite places')


@app.route("/favorites")
def images():
    images = [
        "https://picsum.photos/600/300?random=2",
        "https://picsum.photos/300/150?random=2",
        "https://picsum.photos/600/300?random=2",
        "https://picsum.photos/300/150?random=2",
        "https://picsum.photos/600/300?random=2"
    ]
    return render_template('index.html', images=images )