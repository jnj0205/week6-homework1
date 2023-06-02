from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template('index.html', name='Favorite places')


@app.route("/favorites")
def images():
    image = [
        ('<img src="https://picsum.photos/600/300?random=2" class="rounded mx-auto d-block" alt="...">'),
        ('<img src="https://picsum.photos/600/300?random=2" class="rounded mx-auto d-block" alt="...">'),
        ('<img src="https://picsum.photos/600/300?random=2" class="rounded mx-auto d-block" alt="...">'),
        ('<img src="https://picsum.photos/600/300?random=2" class="rounded mx-auto d-block" alt="...">'),
        ('<img src="https://picsum.photos/600/300?random=2" class="rounded mx-auto d-block" alt="...">')
    ]
    return render_template('index.html' )