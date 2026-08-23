from psycopg_connection import PgManager
import re

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
    
    def get_all(self, user_filter=None):
        if user_filter is None:
            user_filter = {}

        user_fields = ["id", "name", "email", "username", "password", "birthdate", "account_status"]
        # Validate that the keys in user_filter are valid fields
        for key in user_filter.keys():
            if key not in user_fields:
                raise ValueError(f"Invalid filter field: {key}. Valid fields are: {', '.join(user_fields)}")
        try:
            if user_filter:
                filtered_records = self.db_manager.execute_query(
                f"SELECT * FROM lyfter_car_rental.users WHERE { ' AND '.join([f'{key} = %s' for key in user_filter.keys()]) };",
                *user_filter.values() # unpack the values of the user_filter.
                )
                formatted_results = [self._format_user(result) for result in filtered_records]
                return formatted_results
            
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.users;"
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            raise error

    def create(self, user_record):
        try:
            self.db_manager.execute_query(
                """INSERT INTO lyfter_car_rental.users (name, email, username,password,birthdate, account_status) VALUES (%s, %s, %s, %s, %s, %s);""",
                user_record["name"], user_record["email"], user_record["username"], user_record["password"], user_record["birthdate"], user_record["account_status"]
            )
            print("User inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a user into the database: ", error)
            raise error

    def modify(self, user_record):
            user_fields = ["id", "account_status"]
            for key in user_record.keys():
                if key not in user_fields:
                    raise ValueError(f"Invalid filter field: {key}. Valid fields are: {', '.join(user_fields)}")
            try:
                self.db_manager.execute_query(
                    """UPDATE lyfter_car_rental.users SET account_status=%s WHERE id=%s;""",
                    user_record["account_status"], user_record["id"]
                )
                print("User updated successfully")
                return True
            except Exception as error:
                print("Error updating a user in the database: ", error)
                raise error

    def flag_user(self, user_record):
        try:
            self.db_manager.execute_query(
                """UPDATE lyfter_car_rental.users SET account_status= 'Slow Payer' WHERE id=%s;""",
                user_record["id"]
            )
            print("User flagged successfully")
            return True
        except Exception as error:
            print("Error flagging a user in the database: ", error)
            raise error

class CarRepository:
    def __init__(self, psycopg_connection):
        self.db_manager = psycopg_connection

    def _format_car(self, car_record):
        return {
            "id": car_record[0],
            "brand": car_record[1],
            "model": car_record[2],
            "manufacture_year" : car_record[3],
            "car_status": car_record[4],
        }

    def get_all(self, car_filter=None):
        if car_filter is None:
            car_filter = {}

        car_fields = ["id", "brand", "model", "manufacture_year", "car_status"]
        # Validate that the keys in car_filter are valid fields
        for key in car_filter.keys():
            if key not in car_fields:
                raise ValueError(f"Invalid filter field: {key}. Valid fields are: {', '.join(car_fields)}")
        try:
            if car_filter:
                filtered_records = self.db_manager.execute_query(
                f"SELECT * FROM lyfter_car_rental.cars WHERE { ' AND '.join([f'{key} = %s' for key in car_filter.keys()]) };",
                *car_filter.values() # unpack the values of the car_filter.
                )
                formatted_results = [self._format_car(result) for result in filtered_records]
                return formatted_results
            
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.cars;"
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all cars from the database: ", error)
            raise error

    def create(self, car_record):
        try:
            self.db_manager.execute_query(
                """INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status) VALUES (%s, %s, %s, %s);""",
                car_record["brand"], car_record["model"], car_record["manufacture_year"], car_record["car_status"]
            )
            print("Car inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a car into the database: ", error)
            raise error

    def modify(self, car_record):
        car_fields = ["id", "car_status"]
        for key in car_record.keys():
            if key not in car_fields:
                raise ValueError(f"Invalid filter field: {key}. Valid fields are: {', '.join(car_fields)}")
        try:
            self.db_manager.execute_query(
                """UPDATE lyfter_car_rental.cars SET car_status=%s WHERE id=%s;""",
                car_record["car_status"], car_record["id"]
            )
            print("Car updated successfully")
            return True
        except Exception as error:
            print("Error updating a car in the database: ", error)
            raise error

class RentalsRepository:
    def __init__(self, psycopg_connection):
        self.db_manager = psycopg_connection

    def _format_rental(self, rental_record):
        return {
            "id": rental_record[0],
            "user_id": rental_record[1],
            "car_id": rental_record[2],
            "rental_date" : rental_record[3],
            "rental_status": rental_record[4],
        }

    def get_all(self, rental_filter=None):
        if rental_filter is None:
            rental_filter = {}

        rental_fields = ["id", "user_id", "car_id", "rental_date", "rental_status"]
        # Validate that the keys in rental_filter are valid fields
        for key in rental_filter.keys():
            if key not in rental_fields:
                raise ValueError(f"Invalid filter field: {key}. Valid fields are: {', '.join(rental_fields)}")
        try:
            if rental_filter:
                filtered_records = self.db_manager.execute_query(
                f"SELECT * FROM lyfter_car_rental.rentals WHERE { ' AND '.join([f'{key} = %s' for key in rental_filter.keys()]) };",
                *rental_filter.values() # unpack the values of the rental_filter.
                )
                formatted_results = [self._format_rental(result) for result in filtered_records]
                return formatted_results
            
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.rentals;"
            )
            formatted_results = [self._format_rental(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all rentals from the database: ", error)
            raise error

    def create(self, rental_record):
        try:
            self.db_manager.execute_query(
                """DO $$
                DECLARE
                    v_car_id INT := (%s);
                    v_user_id INT := (%s);  -- should be INT, not VARCHAR
                BEGIN
                    -- Check if user exists AND is Active
                    IF NOT EXISTS (
                        SELECT 1
                        FROM lyfter_car_rental.users
                        WHERE id = v_user_id
                        AND account_status = 'Active'
                    ) THEN
                        RAISE EXCEPTION 'User not found or not active.';
                        RETURN;
                    END IF;
                    -- Check if the car is exists AND is Available
                        IF NOT EXISTS (
                        SELECT 1
                        FROM lyfter_car_rental.cars
                        WHERE id = v_car_id
                        AND car_status = 'Available'
                    ) THEN
                        RAISE EXCEPTION 'Car not found or not Available.';
                        RETURN;
                    END IF;


                    -- Create the Rental
                    INSERT INTO lyfter_car_rental.rentals (user_id, car_id)
                    VALUES (v_user_id, v_car_id);

                    RAISE NOTICE 'Rental created successfully.';

                    UPDATE lyfter_car_rental.cars
                    SET car_status = 'Rented'
                    WHERE id = v_car_id;
                END;
                $$;""",
                rental_record["user_id"], rental_record["car_id"]
            )
            print("Rental inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a rental into the database: ", error)
            raise error

    def modify(self, rental_record):
        rental_fields = ["id", "rental_status"]
        for key in rental_record.keys():
            if key not in rental_fields:
                raise ValueError(f"Invalid filter field: {key}. Valid fields are: {', '.join(rental_fields)}")
        if "rental_status" not in rental_record or rental_record["rental_status"] not in ["Active", "Completed", "Cancelled"]:
            raise ValueError("The 'rental_status' must be provided in the rental_record.")
        if rental_record["rental_status"] in ["Active"]:
            raise ValueError("The 'rental_status' should not be active, if you want to complete it must be through 'complete_rental' endpoint.")
        try:
            self.db_manager.execute_query(
                """UPDATE lyfter_car_rental.rentals SET rental_status=%s WHERE id=%s;""",
                rental_record["rental_status"], rental_record["id"]
            )
            print("Rental updated successfully.")
            return True
        except Exception as error:
            print("Error updating a rental in the database: ", error)
            raise error
        
    def complete_rental(self, rental_record):
        rental_fields = ["id"]
        for key in rental_record.keys():
            if key not in rental_fields:
                raise ValueError(f"Invalid filter field: {key}. Valid fields are: {', '.join(rental_fields)}")

        try:
            self.db_manager.execute_query(
                """DO $$
                    DECLARE
                        v_rental_id INT := (%s);
                        v_car_id INT;

                    BEGIN

                        -- Check if rental exists AND is Active
                        IF NOT EXISTS (
                            SELECT 1
                            FROM lyfter_car_rental.rentals
                            WHERE id = v_rental_id
                            AND rental_status = 'Active'
                        ) THEN
                            RAISE EXCEPTION 'Rental not found or not Active.';
                            RETURN;
                        END IF;

                        -- Complete the rental
                        UPDATE lyfter_car_rental.rentals
                        SET rental_status = 'Completed'
                        WHERE id = v_rental_id;

                        SELECT car_id INTO v_car_id
                        FROM lyfter_car_rental.rentals
                        WHERE id = v_rental_id;

                        -- Change the car status
                        UPDATE lyfter_car_rental.cars
                        SET car_status = 'Available'
                        WHERE id = v_car_id;

                        RAISE NOTICE 'Rental finished successfully.';
                    END;
                    $$;""",
                rental_record["id"]
            )
            print("Rental completed successfully.")
            return True
        except Exception as error:
            print("Error completing the rental in the database: ", error)
            raise error