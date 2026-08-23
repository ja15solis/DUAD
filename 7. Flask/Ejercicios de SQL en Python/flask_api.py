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

def body_validation(table,request) -> dict:
    user_required_fields = ['name','username','password','email', 'birthdate', 'account_status']
    cars_required_fields = ['brand', 'model', 'manufacture_year', 'car_status']
    rentals_required_fields = ['user_id', 'car_id']
    cars_status_values = ['Available', 'Reserved', 'Maintenance']
    user_status_values = ['Active', 'Inactive', 'Slow Payer', 'Blocked']

    if table == "users":
        required_fields = user_required_fields
        status_values = user_status_values
    elif table == "cars":
        required_fields = cars_required_fields
        status_values = cars_status_values
    elif table == "rentals":
        required_fields = rentals_required_fields
        status_values = []

    for field in required_fields:
        if field not in request.json:
            raise ValueError(f"The body is missing the {field} field")
        if (field == "account_status" or field == "car_status") and request.json[field].title() not in status_values:
            raise ValueError(f"The status must be one of the following: {status_values}.")
        if field == "email" and not is_valid_email(request.json[field]):
            raise ValueError(f"The email must be a valid email address.")
        if not request.json[field]:
            raise ValueError(f"The {field} must have a value.")

    # return a dictionary with only the required fields and their values
    new_record = {field: request.json[field] for field in required_fields}
    return new_record


@app.route("/lyfter_car_rental/<table>", methods=["GET"])
def get_records(table):
    if table not in ["users", "cars", "rentals"]:
        return jsonify({"message": "Invalid table name. Use 'users', 'cars', or 'rentals'."}), 400
    filters = request.args.to_dict()
    try:
        if table == "users":
            user_repo = UserRepository(db_manager)
            result = user_repo.get_all(filters)
            return jsonify(result), 200
        elif table == "cars":
            car_repo = CarRepository(db_manager)
            result = car_repo.get_all(filters)
            return jsonify(result), 200
        elif table == "rentals":
            rental_repo = RentalsRepository(db_manager)
            result = rental_repo.get_all(filters)
            return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": f"Error retrieving records: {str(e)}"}), 500

@app.route("/lyfter_car_rental/<table>", methods=["POST"])
def create_record(table):
    if table not in ["users", "cars", "rentals"]:
        return jsonify({"message": "Invalid table name. Use 'users', 'cars', or 'rentals'."}), 400
    try:
        new_record = body_validation(table, request) #flask object request is passed to the body_validation function
        if table == "users":
            user_repo = UserRepository(db_manager)
            result = user_repo.create(new_record)
            if result is True:
                return jsonify({"message": "User created successfully."}), 201
        elif table == "cars":
            car_repo = CarRepository(db_manager)
            result = car_repo.create(new_record)
            if result is True:
                return jsonify({"message": "Car created successfully."}), 201
        elif table == "rentals":
            rental_repo = RentalsRepository(db_manager)
            result = rental_repo.create(new_record)
            if result is True:
                return jsonify({"message": "Rental created successfully."}), 201
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error creating record: {str(e)}"}), 500

@app.route("/lyfter_car_rental/users/flag", methods=["PUT"])
def flag_user():
    try:
        request_json = request.get_json()
        user_repo = UserRepository(db_manager)
        result = user_repo.flag_user(request_json)
        if result is True:
            return jsonify({"message": "User flagged successfully."}), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error flagging user: {str(e)}"}), 500

@app.route("/lyfter_car_rental/<table>", methods=["PUT"])
def modify_record(table):
    if table not in ["users", "cars", "rentals"]:
        return jsonify({"message": "Invalid table name. Use 'users', 'cars', or 'rentals'."}), 400
    try:
        request_json = request.get_json()
        if table == "users":
            user_repo = UserRepository(db_manager)
            result = user_repo.modify(request_json)
            if result is True:
                return jsonify({"message": "User modified successfully."}), 200
        elif table == "cars":
            car_repo = CarRepository(db_manager)
            result = car_repo.modify(request_json)
            if result is True:
                return jsonify({"message": "Car modified successfully."}), 200
        elif table == "rentals":
            rental_repo = RentalsRepository(db_manager)
            result = rental_repo.modify(request_json)
            if result is True:
                return jsonify({"message": "Rental modified successfully."}), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error modifying record: {str(e)}"}), 500

@app.route("/lyfter_car_rental/rentals/complete", methods=["PUT"])
def complete_rental():
    try:
        request_json = request.get_json()
        rental_repo = RentalsRepository(db_manager)
        result = rental_repo.complete_rental(request_json)

        if result is True:
            return jsonify({"message": "Rental completed successfully."}), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Error completing rental: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="localhost", debug=True)