from psycopg_connection import PgManager
import csv
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent  # path of the folder containing this .py


db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="postgres",
    host="localhost"
)

db_manager.execute_query("CREATE SCHEMA IF NOT EXISTS lyfter_car_rental;")

db_manager.execute_query(
    """
    CREATE TABLE IF NOT EXISTS lyfter_car_rental.users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        email VARCHAR(40) NOT NULL,
        username VARCHAR(25) NOT NULL,
        password VARCHAR(20) NOT NULL,
        birthdate DATE NOT NULL DEFAULT CURRENT_DATE,
        account_status VARCHAR(20) NOT NULL DEFAULT 'Active'
    );
    """
)

db_manager.execute_query(
    """
    TRUNCATE TABLE lyfter_car_rental.users RESTART IDENTITY;
    """
)

with open(BASE_DIR / "data" / "users_data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        birthdate = datetime.strptime(row["birthdate"], "%d/%m/%Y").date()
        db_manager.execute_query(
            """

            INSERT INTO lyfter_car_rental.users (name, email, username, password, birthdate, account_status)
            VALUES (%s, %s, %s, %s, %s, %s);           
            """,
            row["name"], row["email"], row["username"], row["password"], birthdate, row["account_status"]
)

db_manager.execute_query(
    """
    CREATE TABLE IF NOT EXISTS lyfter_car_rental.cars (
    id SERIAL PRIMARY KEY, 
    brand VARCHAR(20) NOT NULL,
    model VARCHAR(25) NOT NULL,
    manufacture_year INT NOT NULL DEFAULT EXTRACT(YEAR FROM CURRENT_DATE),
    car_status VARCHAR(20) NOT NULL DEFAULT 'Available' 
    );
    """
)

db_manager.execute_query(
    """
    TRUNCATE TABLE lyfter_car_rental.cars RESTART IDENTITY;
    """
)

with open(BASE_DIR / "data"  / "car_data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        db_manager.execute_query(
            """

            INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status)
            VALUES (%s, %s, %s, %s);           
            """,
            row["brand"], row["model"], row["year"], row["status"]
)

db_manager.execute_query(
    """
    CREATE TABLE lyfter_car_rental.rentals (
    id SERIAL PRIMARY KEY, 
    user_id INT NOT NULL REFERENCES lyfter_car_rental.users(id),
    car_id INT NOT NULL REFERENCES lyfter_car_rental.cars(id),
    rental_date DATE NOT NULL DEFAULT CURRENT_DATE,
    rental_status VARCHAR(20) NOT NULL DEFAULT 'Active'
    );
    """
)

db_manager.close_connection()