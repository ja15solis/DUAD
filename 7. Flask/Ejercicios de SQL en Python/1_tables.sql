CREATE TABLE lyfter_car_rental.users (
id SERIAL PRIMARY KEY, -- Different to "INTEGER" SQLite to be added automatically 
name VARCHAR(20) NOT NULL,
email VARCHAR(25) NOT NULL,
username VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL,
birthdate DATE NOT NULL DEFAULT CURRENT_DATE,
account_status VARCHAR(20) NOT NULL DEFAULT 'Active'
);

CREATE TABLE lyfter_car_rental.cars (
id SERIAL PRIMARY KEY, -- Different to "INTEGER" SQLite to be added automatically 
brand VARCHAR(20) NOT NULL,
model VARCHAR(25) NOT NULL,
manufacture_year INT NOT NULL DEFAULT EXTRACT(YEAR FROM CURRENT_DATE),
car_status VARCHAR(20) NOT NULL DEFAULT 'New'
);

CREATE TABLE lyfter_car_rental.rentals (
id SERIAL PRIMARY KEY, 
user_id INT NOT NULL REFERENCES lyfter_car_rental.users(id),
car_id INT NOT NULL REFERENCES lyfter_car_rental.cars(id),
rental_date DATE NOT NULL DEFAULT CURRENT_DATE,
rental_status VARCHAR(20) NOT NULL DEFAULT 'Active'
);