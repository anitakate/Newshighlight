from flask import render_template

from app import app
from .fetch_data import get_sources


@app.route('/')
def index():
    sources = get_sources()
    return render_template("index.html", sources=sources)


@app.route('/about')
def about():
    return render_template("about.html")
