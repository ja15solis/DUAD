from psycopg_connection import PgManager

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

