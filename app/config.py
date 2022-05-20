import os
basedir=os.path.abspath(os.path.dirname(__file__))
class Config(object):
     SECRET_KEY = os.environ.get('SECRET_KEY') or '7771'
     SQLALCHEMY_DATABASE_URI = 'postgresql://ahfxujedqnmymg:f8c2ddde4d20fe7a3a680ec0b69e2bcbfe4216a9ed470da9ccc55f1c9d563aaf@ec2-3-228-235-79.compute-1.amazonaws.com:5432/dqr8jm0hhg9ep'
     SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

    
config_options = {
'development':DevConfig,
}