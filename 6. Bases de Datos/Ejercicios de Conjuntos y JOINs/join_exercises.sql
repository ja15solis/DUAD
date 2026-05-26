-- SQLite
--1
SELECT 
    books.name as book, 
    authors.name as author 
FROM books
LEFT JOIN authors 
    ON authors.id = books.author_id
;

--2 
SELECT 
    books.name as book
FROM books
WHERE author_id IS NULL 
;

--3
SELECT 
    authors.name as author 
FROM authors
LEFT JOIN books
    ON authors.id = books.author_id
WHERE books.author_id IS NULL
;

--4
SELECT DISTINCT
    books.name as book
FROM books
INNER JOIN rents
    ON books.id = rents.book_id
;

--5
SELECT 
    books.name as book
FROM books
LEFT JOIN rents
    ON books.id = rents.book_id
WHERE rents.book_id IS NULL
;

--6
SELECT 
    customers.name AS customer
FROM customers
LEFT JOIN rents
    ON customers.id = rents.customer_id
WHERE rents.customer_id IS NULL
;

--7
SELECT DISTINCT
    books.name as book
FROM books
INNER JOIN rents
    ON books.id = rents.book_id
WHERE rents.rent_state = "Overdue"
;