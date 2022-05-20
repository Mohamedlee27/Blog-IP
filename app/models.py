from app import db
from app import login
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    blogs = db.relationship('Blog', backref='author', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')

    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
@login.user_loader
def load_user(id):
    return User.query.get(int(id))




class Blog(db.Model):
    
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(30))
    sub_title=db.Column(db.String(20))
    content=db.Column(db.String(300))
    time_posted=db.Column(db.DateTime,index=True, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment = db.relationship('Comment', backref='pitch', lazy='dynamic')


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_blog(id):
        blog = Blog.query.filter_by(id=id).first()
        return blog

    def __repr__(self):
        return f'Blog {self.title}'
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = False)
    blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'),nullable = False)
    

    def save_c(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,blog_id):
        comments = Comment.query.filter_by(blog_id=blog_id).all()
        return comments

    
    def __repr__(self):
        return f'comment:{self.comment}'
    
