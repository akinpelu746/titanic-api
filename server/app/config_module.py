
# Config Class 
class Config(object):
    TESTING = False
    DEBUG = False

class ProductionConfig(Config):
   MONGODB_HOST=  'mongodb://localhost:27017/titanic'
   DEBUG = True


class DevelopmentConfig(Config):
   MONGODB_HOST= 'mongodb://localhost:27017/dev'
   DEBUG = True
   DEVELOPMENT = True


class TestingConfig(Config):
    MONGODB_HOST= 'mongodb://localhost:27017/test'
    TESTING = True
    DEBUG = True


config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
    'testing': TestingConfig,
}