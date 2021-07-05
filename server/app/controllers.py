from  database.models import Passenger 
from flask import abort
class PassengersActions:
    def save_people(self,record):
        passeneger = Passenger(**record)
        try:
            passeneger.save()
        except Passenger.DoesNotExist:
            abort(400,"Passenegr Parameter Missing")
        body = passeneger.to_dict()
        return {"message":"User created successfully","data":body}

    def get_people(self):
        people_lists = [movie.to_dict() for movie in Passenger.objects]
        return {"message":"Succesful","data":people_lists}
    
    def get_people_by_uuid(self,uuid):
        try:
            people = Passenger.objects.get(_id=uuid)
        except Passenger.DoesNotExist:
            abort(400, 'USER NOT FOUND')   
        people = people.to_dict()
        return {"data":people,"message":"succesful"}

    
    def delete_by_uuid(self,uuid):
        try:
             people = Passenger.objects.get(_id=uuid)
        except Passenger.DoesNotExist:
            abort(400, 'USER NOT FOUND') 
        people.delete()

    
    def update_by_uuid(self,uuid,body):
        try:
            people = Passenger.objects.get(_id=uuid)
        except Passenger.DoesNotExist:
            abort(400, 'USER NOT FOUND')        
        people.update(**body)
