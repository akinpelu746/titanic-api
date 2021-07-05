from flask_mongoengine import MongoEngine

db = MongoEngine()

#Intialize the database
def initialize_db(app):
    db.init_app(app)