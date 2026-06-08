DO $$
DECLARE
    v_user_id INT; -- The user making the purchase -- created as null
    v_stock INT;
    v_bill_id INT;
    v_item RECORD;
    -- v_product_id INT;
    -- v_quantity INT;
    v_total DECIMAL(8,2) := 0;
BEGIN
    --temporary table with items
    CREATE TEMP TABLE IF NOT EXISTS bill_items (
        product_id INT,
        quantity INT
    ) ON COMMIT DROP; -- to drop the table automatically when the transaction ends

    INSERT INTO bill_items (product_id, quantity)
    VALUES (1,10), (2,4), (11,1);


    -- 1. verify user exists
    SELECT id INTO v_user_id
    FROM users
    WHERE id = 1;

    IF v_user_id IS NULL
        THEN RAISE EXCEPTION 'User not found';
    END IF;

    -- 2. check stock for each product
    FOR v_item IN (SELECT * FROM bill_items) --MULTIPLE ID PRODUCTS AND QUANTITY
    LOOP
        SELECT 
            stock INTO v_stock
        FROM products
        WHERE id = v_item.product_id;

        IF IFNULL(v_stock,0) < v_item.quantity --IFNULL(v_stock,0) for products not in the DATABASE
            THEN RAISE EXCEPTION 'No stock in this product id: %', v_product_id;
        END IF;
    END LOOP;

    -- 3. insert bill
    INSERT INTO bills (user_id) 
    VALUES (v_user_id)
    RETURNING id INTO v_bill_id; --assign a variable once the record is created

    -- 4. Insert bills_products
    FOR v_item IN (SELECT * FROM bill_items)
    LOOP
        INSERT INTO bills_products (product_id,bill_id,quantity)
        VALUES(v_item.product_id,v_bill_id,v_item.quantity);
    END LOOP;
    -- 5. Update stock
    FOR v_item IN (SELECT * FROM bill_items)
    LOOP
        UPDATE products
        SET stock = (stock -  v_item.quantity)
        WHERE id = v_item.product_id;
    END LOOP;
    -- 6. Update bill total
    SELECT SUM(products.price * bills_products.quantity) INTO v_total --save total into the variable
    FROM bills_products
    JOIN products
        ON bills_products.product_id = products.id
    WHERE bills_products.bill_id = v_bill_id;

    UPDATE bills
    SET total = v_total
    WHERE id = v_bill_id;
    


END;
$$;