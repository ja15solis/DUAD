1

SELECT * FROM products
;
--2
SELECT * FROM products
WHERE price > 50000
;
--3
SELECT product_id, SUM(quantity) AS quantity
FROM invoice_items
WHERE product_id = 3
GROUP BY product_id
;
--4
SELECT product_id, SUM(quantity) AS quantity, SUM(total_amount) as total_amount
FROM invoice_items
GROUP BY product_id
;
--5
SELECT invoice_number
FROM invoices
WHERE buyer_email = "javier@gmail.com"
;
--6
SELECT * FROM invoices
ORDER BY total_amount DESC
;
--7
SELECT * FROM invoices
WHERE invoice_number = 12351425
