#core/app.py
from flask import render_template
from core import app, db

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

