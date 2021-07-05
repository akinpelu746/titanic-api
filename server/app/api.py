from flask import jsonify
from flask import request
from mongoengine.errors import ValidationError
from database.db import initialize_db
from controllers import PassengersActions
from flask import Flask ,  jsonify
from dotenv import load_dotenv
import os
from  config_module import config



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    if os.environ.get('MONGODB_USERNAME') != None and os.environ.get('MONGODB_PASSWORD') != None :
        app.config['MONGODB_SETTINGS'] = {
    'connect': False,
    'host': 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOST'] + ':27017/' + os.environ['MONGODB_DB'] + '?authSource='  + os.environ['authenticationDB']
    }
    else:
        app.config.from_object(config.get(config_name or 'dev'))
    initialize_db(app)
    return app





passenger = PassengersActions()



load_dotenv()

app = create_app(os.environ['ENV'])
app.debug = True



   


# Just a health check
@app.route("/")
def url_root():
    return "OK"

# Get all passeneger
@app.route("/people", methods=['GET'])
def url_get_all():
    return jsonify(passenger.get_people()),200

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



@app.errorhandler(404)
def handle_invalid_usage(error):
    response = jsonify({'error': error.description})
    response.status_code = error.code
    response.content_type = "application/json"

    return response

@app.errorhandler(ValidationError)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = jsonify({'error': e.field_name + ' '  + e.message})
    response.status_code = 400
    response.content_type = "application/json"
    return response





if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
