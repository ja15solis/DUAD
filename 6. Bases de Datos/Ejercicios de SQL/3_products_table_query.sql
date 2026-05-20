-- SQLite
CREATE TABLE products (
id INTEGER PRIMARY KEY, --"INTEGER" To be added automatically 
code VARCHAR(25) NOT NULL,
name VARCHAR(40) NOT NULL,
price FLOAT DEFAULT 0,
entry_date TEXT NOT NULL DEFAULT CURRENT_DATE,
brand VARCHAR(25) ,
stock_available BIGINT DEFAULT 0
);