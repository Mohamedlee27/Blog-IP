from app import app,db
from flask import render_template,flash,url_for,redirect,abort,request
from app.forms import LoginForm, RegistrationForm, BlogForm,CommentForm
from app.models import User, Blog,Comment
from flask_login import current_user, login_user,logout_user
from .requests import get_quotes



blogs = [
    { 
      'title'  :'Interface Design',
      'content'  :'Animation is like cursing. If you overuse it, it loses all its impact.',
      'time_posted' : 'October 17 2002'
    },
]

@app.route('/')
def index():
    quote = get_quotes()
    return render_template('index.html',quote=quote)

@app.route('/blog')
def blog():
    blogs=Blog.query.all()
    return render_template('blog.html',blog=blogs)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form=LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash(f'Invalid username or password', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        return redirect(url_for('index'))
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
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))

# @app.route('/new')
# def new():
#     form=BlogForm()

#     return render_template('newblog.html' ,form=form)

@app.route('/newblog', methods=['POST', 'GET'])
def newPost():
    form=BlogForm()
    if form.validate_on_submit():
        blog=Blog(title=form.title.data , sub_title=form.sub_title.data, content=form.content.data )
        db.session.add(blog)
        db.session.commit()
        flash('blog added succesfully')
        return redirect(url_for('blog'))
    return render_template('newblog.html' ,form=form)

@app.route('/blog/<blog_id>/delete', methods = ['POST'])
def delete_post(blog_id):
    blog = Blog.query.get(blog_id)
    blog.delete()

    flash("You have deleted your Blog succesfully!")
    return redirect(url_for('blog'))
@app.route('/blog/<blog_id>/update', methods = ['GET','POST'])
def updateblog(blog_id):
    blog = Blog.query.get(blog_id)
    form = BlogForm()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.sub_title = form.sub_title.data
        blog.content = form.content.data
        db.session.commit()
        flash("You have updated your Blog!")
        return redirect(url_for('blog',id = blog.id)) 
    if request.method == 'GET':
        form.sub_title.data = blog.sub_title
        form.title.data = blog.title
        form.content.data = blog.content
    return render_template('newblog.html', form = form)

@app.route('/comment/<int:blog_id>', methods = ['POST','GET'])
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,blog_id = blog_id)
        new_comment.save_c()
        return redirect(url_for('.comment', blog_id = blog_id))
    return render_template('comment.html', form =form, blog = blog,all_comments=all_comments)
