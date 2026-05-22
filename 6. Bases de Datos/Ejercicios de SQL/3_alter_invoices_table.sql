-- SQLite
ALTER TABLE invoices 
    ADD customer_phone_number VARCHAR(13);

ALTER TABLE invoices 
    ADD cashier_code VARCHAR(10);

--SQLite does not support multiple columns in an alter table statement
