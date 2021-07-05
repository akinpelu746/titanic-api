import pytest
from test_client import client,new_user
from app.database.models import  Passenger
import unittest


class TestMath(unittest.TestCase):
    def test_health(client):
        response = client.get('/')
        assert response.status_code == 200
        assert  b'login' in response.data



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert  b'login' in response.data


def test_get_route(client,new_user):
    new_user.save()
    response = client.get('/people')
    assert response.status_code == 200
    assert  response.json['Message'] == 'Succesful'
    assert response.json(['Data'])  == new_user
    assert response.content_type == 'application/json'



def test_user(new_user):
    new_user.save()
    all_users = list(Passenger.objects.all())
    assert_that(all_users, has_length(1))
    




# Save a passeneger
@app.route("/people",methods=['POST'])
def url_save():
    body = request.get_json(force=True)
    return jsonify(passenger.save_people(body)),201



# Get a passeneger
@app.route("/people/<uuid>",methods=["GET"])
def url_get(uuid):
    return jsonify(passenger.get_people_by_uuid(uuid)),200



# Delete Passenger
@app.route("/people/<uuid>", methods = ["DELETE"])
def url_delete(uuid):
    return jsonify(passenger.delete_by_uuid(uuid)),202



# Updating a passenger
@app.route("/people/<uuid>",methods = ["PUT"])
def url_update_passenger(uuid):
    body = request.get_json()
    return jsonify(passenger.update_by_uuid(uuid,body)), 202



































