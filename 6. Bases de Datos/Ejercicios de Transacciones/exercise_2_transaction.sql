DO $$
DECLARE
    v_user_id INT := 1; -- The user making the purchase
    v_stock INT;
    v_bill_id INT;
    v_product_id INT;
    v_quantity INT;
    v_total DECIMAL(8,2) := 0;
BEGIN
    -- 1. verify user exists
    SELECT id INTO v_user_id
    FROM users
    WHERE id = 1;

    IF v_user_id IS NULL
        THEN RAISE EXCEPTION 'User not found';
    END IF;

    -- 2. check stock for each product
    FOR v_product_id, v_quantity IN 
        VALUES (1,10),(2,4),(11,1) --MULTIPLE ID PRODUCTS AND QUANTITY
    LOOP
        SELECT 
            stock INTO v_stock
        FROM products
        WHERE id = v_product_id;

        IF v_stock < v_quantity
            THEN RAISE EXCEPTION 'No stock in this product id: %', v_product_id;
        END IF;
    END LOOP;

    -- 3. insert bill
    INSERT INTO bills (user_id) 
    VALUES (v_user_id)
    RETURNING id INTO v_bill_id; --assign a variable once the record is created

    -- 4. Insert bills_products
    FOR v_product_id, v_quantity IN 
        VALUES (1,10),(2,4),(11,1)
    LOOP
        INSERT INTO bills_products (product_id,bill_id,quantity)
        VALUES(v_product_id,v_bill_id,v_quantity);
    END LOOP;
    -- 5. Update stock
    FOR v_product_id, v_quantity IN 
        VALUES (1,10),(2,4),(11,1)
    LOOP
        UPDATE products
        SET stock = (stock - v_quantity)
        WHERE id = v_product_id;
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