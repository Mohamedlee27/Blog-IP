from app import app,db
from flask import render_template,flash,url_for,redirect
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import login_user
from flask_login import current_user, login_user
@app.route('/')
@app.route('/home')
def home():

    return render_template('index.html')



@app.route('/login', methods=['POST', 'GET'])
def login():
    form=LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash(f'Invalid username or password', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/reg',  methods=['POST', 'GET'])
def registration():
    form=RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account succesfully created', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)


