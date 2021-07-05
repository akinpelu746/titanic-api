import pytest
from app import api

from  app.database.models  import  Passenger
from app.config_module import config


@pytest.fixture
def client():
    app = api.create_app(config.get('test'))
    app.config['TESTING'] = True

    with app.app_context():
        with app.tes_client() as client:
            yield client



@pytest.fixture(scope='module')
def new_user():
    passeneger = Passenger( survived= True, passengerClass= 21, name= "Mr. Owen Harris Braund", sex = "male", age= 22, siblingsOrSpousesAboard= 1, parentsOrChildrenAboard=0, fare=7.25)
    return passeneger