-- SQLite
CREATE TABLE invoices (
id INTEGER PRIMARY KEY, --"INTEGER" To be added automatically 
shopping_cart_id INT REFERENCES shopping_cart(id),
invoice_number BIGINT,
purchase_date TEXT DEFAULT CURRENT_DATE,
buyer_email TEXT NOT NULL,
total_ammount FLOAT NOT NULL DEFAULT 0
);
