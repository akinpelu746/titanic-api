from database.db import db
from bson.objectid import ObjectId
from mongoengine import *


# Data Model
class Passenger(db.Document):
    # Use existing Collection
    meta = {'collection' : 'Passeneger' }
    
    _id = db.ObjectIdField( primary_key= True, required=True, default=lambda: ObjectId() )
    survived  = db.BooleanField(required=True)
    passengerClass  =  db.IntField(required=True)
    name =  db.StringField(max_length=120, required=True)
    sex = db.StringField(choices=['male', 'female'], required=True)
    age = db.IntField(min_value=0,required=True)
    parentsOrChildrenAboard =  db.IntField(min_value=0,required=True)
    siblingsOrSpousesAboard = db.IntField(min_value=0,required=True)
    fare =  db.FloatField(min_value=0,required=True)


    def to_dict(self):
        return { 
        "uuid": str(self._id),
        "survived": self.survived,
        "passengerClass": self.passengerClass,
        "name": self.name,
        "sex": self.sex,
        "age": self.age,
        "parentsOrChildrenAboard": self.parentsOrChildrenAboard,
        "siblingsOrSpousesAboard": self.siblingsOrSpousesAboard,
        "fare": self.fare,
    }






