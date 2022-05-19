from app import app
from flask import render_template
from app.forms import LoginForm, RegistrationForm
@app.route('/')
@app.route('/home')
def home():

    return render_template('index.html')



@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/reg')
def registration():
    return render_template('registration.html')

