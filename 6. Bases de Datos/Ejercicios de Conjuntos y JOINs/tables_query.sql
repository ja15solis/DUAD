-- Tables
CREATE TABLE books (
id INTEGER PRIMARY KEY, --"INTEGER" To be added automatically 
name VARCHAR(50) NOT NULL,
author INT REFERENCES authors (id)
);

CREATE TABLE authors (
id INTEGER PRIMARY KEY, --"INTEGER" To be added automatically 
name VARCHAR(50) NOT NULL
);

CREATE TABLE customers (
id INTEGER PRIMARY KEY, --"INTEGER" To be added automatically 
name VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL
);

CREATE TABLE rents (
id INTEGER PRIMARY KEY, --"INTEGER" To be added automatically 
book_id INT NOT NULL REFERENCES books (id),
customer_id INT NOT NULL REFERENCES customers (id),
rent_state VARCHAR(15) NOT NULL
);

