CREATE TABLE users (
id SERIAL PRIMARY KEY, -- Different to "INTEGER" SQLite to be added automatically 
name VARCHAR(20) NOT NULL,
email VARCHAR(25) NOT NULL
);

CREATE TABLE products (
id SERIAL PRIMARY KEY, 
name TEXT NOT NULL,
stock INT NOT NULL,
price DECIMAL(8,2) NOT NULL DEFAULT 0
);

CREATE TABLE bills (
id SERIAL PRIMARY KEY,
bill_date DATE NOT NULL DEFAULT CURRENT_DATE,
user_id INT NOT NULL REFERENCES users(id),
total DECIMAL(8,2) NOT NULL DEFAULT 0,
status VARCHAR(20) NOT NULL DEFAULT 'Active' --use single quotes
);

CREATE TABLE bills_products (
id SERIAL PRIMARY KEY, 
product_id INT NOT NULL REFERENCES products(id),
bill_id INT NOT NULL REFERENCES bills(id),
quantity INT NOT NULL
);
