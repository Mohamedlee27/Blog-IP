from app import app,db
from flask import render_template,flash,url_for,redirect
from app.forms import LoginForm, RegistrationForm, BlogForm
from app.models import User, Blog
from flask_login import login_user
from flask_login import current_user, login_user
@app.route('/')
@app.route('/home')
def home():
    blogs=Blog.query.all()
    return render_template('index.html',blogs=blogs)



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

@app.route('/new')
def new():
    form=BlogForm()

    return render_template('newblog.html' ,form=form)

@app.route('/newblog', methods=['POST', 'GET'])
def newPost():
    form=BlogForm()
    if form.validate_on_submit:
        blog=Blog(title=form.title.data , sub_title=form.sub_title.data, content=form.content.data )
        db.session.add(blog)
        db.session.commit()
        flash('blog added succesfully')
        return redirect(url_for('home'))

