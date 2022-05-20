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
    # comments=db.relationship('Comment' ,backref='writer', lazy='dynamic')
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
@login.user_loader
def load_user(id):
    return User.query.get(int(id))




class Blog(UserMixin,db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(30))
    sub_title=db.Column(db.String(20))
    content=db.Column(db.String(300))
    time_posted=db.Column(db.DateTime,index=True, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
