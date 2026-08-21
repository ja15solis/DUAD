from psycopg_connection import PgManager
import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

class UserRepository:
    def __init__(self, psycopg_connection):
        self.db_manager = psycopg_connection

    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "name": user_record[1],
            "email": user_record[2],
            "username" : user_record[3],
            "password": user_record[4],
            "birthdate" : user_record[5],
            "account_status": user_record[6],
        }

    def body_validation_user(self,user_record):
        required_tasks_fields = ["name", "email", "username", "password"]
        id_records = []
        username_records = []

        for field in required_tasks_fields:
            if field == "id":
                #CHECK IF THAT RECORD EXIST and if the method is create, or if the id doesnt exist and the method is different than create.
                #IF IT DOES RAISE A VALUEERROR
                raise ValueError(f"The id already exist in the database, you don't need to input the id if you want to create a new record.")
                raise ValueError(f"To edit or delete a record, you need to provide an 'id'.")
            if field == "username" and user_record.json[field].lowercase() in username_records: ##
                raise ValueError(f"The username already exist in the database, please select another one.")
            if field == "email" and not is_valid_email(user_record.json[field]): ##
                raise ValueError(f"Please enter a valid email.")
            if not user_record.json[field]:
                raise ValueError(f"The {field} must have a value.")
        # Validation for id
        try:
            task_id = int(user_record.json["task_id"])
        except (ValueError, TypeError):
            raise ValueError(f"The task_id must be a valid integer.")
        # create new task
        new_user = {field: user_record.json[field] for field in required_tasks_fields}
        new_user["id"] = task_id 
        return new_user

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.users;"
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False

    def create(self, name, email, username,password,birthdate):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.cars (name, email, username,password,birthdate) VALUES (%s, %s, %s, %s, %s)",
                (name, email, username,password,birthdate),
            )
            print("User inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a user into the database: ", error)
            return False

class CarRepository:
    def __init__(self, psycopg_connection):
        self.db_manager = psycopg_connection

    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "brand": user_record[1],
            "model": user_record[2],
            "manufacture_year" : user_record[3],
            "car_status": user_record[4],
        }

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.cars;"
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False

    def create(self, brand, model, manufacture_year):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year) VALUES (%s, %s, %s)",
                (brand, model, manufacture_year),
            )
            print("Car inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a user into the database: ", error)
            return False

