-- SQLite
CREATE TABLE invoice_items (
id INTEGER PRIMARY KEY, --"INTEGER" To be added automatically 
product_id INT NOT NULL REFERENCES products(id),
invoice_id INT NOT NULL REFERENCES invoices(id),
quantity FLOAT NOT NULL DEFAULT 0,
total_amount FLOAT NOT NULL DEFAULT 0
);