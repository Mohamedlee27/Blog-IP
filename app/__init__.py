from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import  Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
app=Flask(__name__)
app.config.from_object(Config)
app.config[' SQLALCHEMY_DATABASE_URI']='postgresql://ahfxujedqnmymg:f8c2ddde4d20fe7a3a680ec0b69e2bcbfe4216a9ed470da9ccc55f1c9d563aaf@ec2-3-228-235-79.compute-1.amazonaws.com:5432/dqr8jm0hhg9ep'
db=SQLAlchemy(app)
bootstrap.init_app(app)

migrate=Migrate(app, db)
login=LoginManager(app)





from app import views,models