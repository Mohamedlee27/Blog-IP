import os
basedir=os.path.abspath(os.path.dirname(__file__))
class Config(object):
     SECRET_KEY = os.environ.get('SECRET_KEY') or '7771'
     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
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