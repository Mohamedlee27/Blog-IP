from app import app
from flask import render_template
from app.forms import LoginForm, RegistrationForm
@app.route('/')
@app.route('/home')
def home():

    return render_template('index.html')



@app.route('/login', methods=['POST', 'GET'])
def login():
    form=LoginForm()
    return render_template('login.html', form=form)


@app.route('/reg',  methods=['POST', 'GET'])
def registration():
    return render_template('registration.html')

