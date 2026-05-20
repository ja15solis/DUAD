-- SQLite
CREATE TABLE invoices (
id INTEGER PRIMARY KEY, --"INTEGER" To be added automatically 
shopping_cart_id INT REFERENCES shopping_cart(id),
invoice_number BIGINT UNIQUE,
purchase_date TEXT DEFAULT CURRENT_DATE,
buyer_email TEXT NOT NULL,
total_amount FLOAT NOT NULL DEFAULT 0
);
