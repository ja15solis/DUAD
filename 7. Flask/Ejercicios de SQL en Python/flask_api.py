import psycopg2
from psycopg_connection import PgManager
from repository_pattern import UserRepository
from repository_pattern import CarRepository
from repository_pattern import RentalsRepository
from flask import Flask, jsonify, request
import re

app = Flask(__name__)

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="postgres",
    host="localhost"
)

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def body_validation(required_fields, status_field, status_values) -> dict:
    body = request.get_json()
    if not body:
        raise ValueError("Missing JSON body.")
    for field in required_fields:
        if field not in body:
            raise ValueError(f"The body is missing the '{field}' field.")
        if field == status_field and body[field].title() not in status_values:
            raise ValueError(f"'{field}' must be one of: {status_values}.")
        if field == "email" and not is_valid_email(body[field]):
            raise ValueError("The email must be a valid email address.")
        if not body[field] and body[field] != 0:
            raise ValueError(f"'{field}' must have a value.")
    return {field: body[field].title() if field == status_field else body[field] for field in required_fields}


# Users
@app.route("/lyfter_car_rental/users", methods=["GET"])
def get_users():
    filters = request.args.to_dict()
    try:
        repo = UserRepository(db_manager)
        result = repo.get_all(filters)
        return jsonify(result), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error retrieving users: {str(e)}"}), 500

@app.route("/lyfter_car_rental/users", methods=["POST"])
def create_user():
    try:
        new_record = body_validation(
            required_fields=['name', 'username', 'password', 'email', 'birthdate', 'account_status'],
            status_field='account_status',
            status_values=['Active', 'Inactive', 'Slow Payer', 'Blocked']
        )
        repo = UserRepository(db_manager)
        repo.create(new_record)
        return jsonify({"message": "User created successfully."}), 201
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error creating user: {str(e)}"}), 500

@app.route("/lyfter_car_rental/users/<int:id>", methods=["PUT"])
def modify_user(id):
    try:
        body = request.get_json()
        if not body:
            raise ValueError("Missing JSON body.")
        repo = UserRepository(db_manager)
        repo.modify({"id": id, "account_status": body["account_status"]})
        return jsonify({"message": "User modified successfully."}), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error modifying user: {str(e)}"}), 500

@app.route("/lyfter_car_rental/users/<int:id>/flag", methods=["PUT"])
def flag_user(id):
    try:
        repo = UserRepository(db_manager)
        repo.flag_user({"id": id})
        return jsonify({"message": "User flagged successfully."}), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error flagging user: {str(e)}"}), 500


# Cars
@app.route("/lyfter_car_rental/cars", methods=["GET"])
def get_cars():
    filters = request.args.to_dict()
    try:
        repo = CarRepository(db_manager)
        result = repo.get_all(filters)
        return jsonify(result), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error retrieving cars: {str(e)}"}), 500

@app.route("/lyfter_car_rental/cars", methods=["POST"])
def create_car():
    try:
        new_record = body_validation(
            required_fields=['brand', 'model', 'manufacture_year', 'car_status'],
            status_field='car_status',
            status_values=['Available', 'Reserved', 'Maintenance']
        )
        repo = CarRepository(db_manager)
        repo.create(new_record)
        return jsonify({"message": "Car created successfully."}), 201
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error creating car: {str(e)}"}), 500

@app.route("/lyfter_car_rental/cars/<int:id>", methods=["PUT"])
def modify_car(id):
    try:
        body = request.get_json()
        if not body:
            raise ValueError("Missing JSON body.")
        repo = CarRepository(db_manager)
        repo.modify({"id": id, "car_status": body["car_status"]})
        return jsonify({"message": "Car modified successfully."}), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error modifying car: {str(e)}"}), 500


# Rentals

@app.route("/lyfter_car_rental/rentals", methods=["GET"])
def get_rentals():
    filters = request.args.to_dict()
    try:
        repo = RentalsRepository(db_manager)
        result = repo.get_all(filters)
        return jsonify(result), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error retrieving rentals: {str(e)}"}), 500

@app.route("/lyfter_car_rental/rentals", methods=["POST"])
def create_rental():
    try:
        new_record = body_validation(
            required_fields=['user_id', 'car_id'],
            status_field=None,
            status_values=[]
        )
        repo = RentalsRepository(db_manager)
        repo.create(new_record)
        return jsonify({"message": "Rental created successfully."}), 201
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error creating rental: {str(e)}"}), 500

@app.route("/lyfter_car_rental/rentals/<int:id>", methods=["PUT"])
def modify_rental(id):
    try:
        body = request.get_json()
        if not body:
            raise ValueError("Missing JSON body.")
        repo = RentalsRepository(db_manager)
        repo.modify({"id": id, "rental_status": body["rental_status"]})
        return jsonify({"message": "Rental modified successfully."}), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error modifying rental: {str(e)}"}), 500

@app.route("/lyfter_car_rental/rentals/<int:id>/complete", methods=["PUT"])
def complete_rental(id):
    try:
        repo = RentalsRepository(db_manager)
        repo.complete_rental({"id": id})
        return jsonify({"message": "Rental completed successfully."}), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error completing rental: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="localhost", debug=True)