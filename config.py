import psycopg2
class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lee:lee123@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY='1234'