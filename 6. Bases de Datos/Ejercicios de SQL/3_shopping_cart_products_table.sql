-- SQLite
CREATE TABLE shopping_cart_products (
id INTEGER PRIMARY KEY, --"INTEGER" To be added automatically 
shopping_cart_id INT NOT NULL REFERENCES shopping_cart(id),
product_id INT NOT NULL REFERENCES products(id)
);