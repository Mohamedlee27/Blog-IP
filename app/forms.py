import email
from click import confirm
from flask import Flask
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email,EqualTo, ValidationError,Length
from wtforms import StringField,SubmitField,TextAreaField,PasswordField,BooleanField
# from app.models import User



class LoginForm(FlaskForm):
    email=StringField('Email', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    remember=BooleanField('Remember me?')
    submit=SubmitField('Login')

class RegistrationForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email=StringField('Email', validators=[DataRequired()])
    password=PasswordField('Password', validators=[DataRequired()])
    confirm_password=PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Sign up')



