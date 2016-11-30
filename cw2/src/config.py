#default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'my-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
