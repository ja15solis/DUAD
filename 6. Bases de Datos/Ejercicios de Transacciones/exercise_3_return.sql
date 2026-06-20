
DO $$
DECLARE
    v_bill_id INT;
    v_bill_status VARCHAR(25);
    v_product RECORD; --this can hold any data row structure 
BEGIN
    -- 1. verify bill exists
    SELECT 
        id, status
        INTO v_bill_id, v_bill_status
    FROM bills
    WHERE id = 1; --bill returned

    IF v_bill_id IS NULL THEN
        RAISE EXCEPTION 'The bill does not exist';
    END IF;

    IF v_bill_status = 'Returned'
        THEN RAISE EXCEPTION 'The bill has already been returned.';
    END IF;
    
    -- 2. Return the quantity to the stock
    FOR v_product IN 
        (
        SELECT 
            product_id,
            quantity
        FROM bills_products
        WHERE bill_id = v_bill_id
        )
    LOOP
        UPDATE products
        SET stock = stock + v_product.quantity
        WHERE id = v_product.product_id;
    END LOOP;
    -- 3. Set the bill to returned
    UPDATE bills
        SET status = 'Returned'
        WHERE id = v_bill_id;
END;
$$;