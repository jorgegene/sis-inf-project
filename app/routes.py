from flask import render_template, flash, redirect, url_for, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/profile')
def about():
    return render_template('profile.html')