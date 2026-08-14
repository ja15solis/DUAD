-- 1. Un script que agregue un usuario nuevo

INSERT INTO lyfter_car_rental.users (name, email, username, password, birthdate)
            VALUES ("Javier Solis", "javier@email.com", "javiersolis", "1239487ahdf9", "1997-05-15");           

-- 2. Un script que agregue un automovil nuevo

INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year)
            VALUES ("Toyota", "Corolla", 2016);    

-- 3. Un script que cambie el estado de un usuario
UPDATE lyfter_car_rental.users
SET account_status = "Inactive"
WHERE name="Javier Solis";

--Un script que cambie el estado de un automovil
UPDATE lyfter_car_rental.cars
SET car_status = "Maintenance"
WHERE id = 101;

-- 4. Un script que genere un alquiler nuevo con los datos de un usuario y un automovil

DO $$
DECLARE
    v_car_id INT := 1;
    v_user_id INT := 2;  -- should be INT, not VARCHAR
BEGIN
    -- Check if user exists AND is Active
    IF NOT EXISTS (
        SELECT 1
        FROM lyfter_car_rental.users
        WHERE id = v_user_id
        AND account_status = 'Active'
    ) THEN
        RAISE NOTICE 'User not found or not active.';
        RETURN;
    END IF;
    -- Check if the car is exists AND is Available
        IF NOT EXISTS (
        SELECT 1
        FROM lyfter_car_rental.cars
        WHERE id = v_car_id
        AND car_status = 'Available'
    ) THEN
        RAISE NOTICE 'Car not found or not Available.';
        RETURN;
    END IF;


    -- Create the Rental
    INSERT INTO lyfter_car_rental.rentals (user_id, car_id)
    VALUES (v_user_id, v_car_id);

    RAISE NOTICE 'Rental created successfully.';

    UPDATE lyfter_car_rental.cars
    SET car_status = "Rented"
    WHERE id = v_car_id;
END;
$$;


-- 5. Un script que confirme la devolución del auto al completar el alquiler, colocando el auto como disponible y completando el estado del alquiler

DO $$
DECLARE
    v_rental_id INT := 51;
    v_car_id INT;

BEGIN

    -- Check if rental exists AND is Active
    IF NOT EXISTS (
        SELECT 1
        FROM lyfter_car_rental.rental
        WHERE id = v_rental_id
        AND rental_status = 'Active'
    ) THEN
        RAISE NOTICE 'Rental not found or not Active.';
        RETURN;
    END IF;

    -- Complete the rental
    UPDATE lyfter_car_rental.rental
    SET car_status = "Inactive"
    WHERE id = v_rental_id;

    SELECT car_id INTO v_car_id
    FROM lyfter_car_rental.rental
    WHERE id = v_rental_id;

    -- Change the car status
    UPDATE lyfter_car_rental.cars
    SET car_status = "Available"
    WHERE id = v_car_id;

    RAISE NOTICE 'Rental finished successfully.';
END;
$$;

-- 6. Un script que deshabilite un automovil del alquiler
DO $$
DECLARE
    v_car_id INT := 1;
    v_car_status = "Maintenance";
BEGIN

    -- Check if the car is currently rented
    IF EXISTS (
        SELECT 1
        FROM lyfter_car_rental.rental
        WHERE car_id = v_rental_id
        AND rental_status = 'Active'
    ) THEN
        RAISE NOTICE 'Car not found or with active rental, the status of the car can not be changed.';
        RETURN;
    END IF;

    -- Complete the change
    UPDATE lyfter_car_rental.cars
    SET car_status = v_car_status
    WHERE id = v_car_id;

    RAISE NOTICE 'Status of the Car changed successfully.';
END;
$$;

-- 7. Un script que obtenga todos los automoviles alquilados, y otro que obtenga todos los disponibles.
SELECT * FROM lyfter_car_rental.cars
WHERE car_status = "Rented";

SELECT * FROM lyfter_car_rental.cars
WHERE car_status = "Available";
