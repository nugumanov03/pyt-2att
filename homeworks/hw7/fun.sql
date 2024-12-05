-- Creating function in db
DELIMITER $$

CREATE FUNCTION calculate_bonus(salary DECIMAL(10, 2))
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    DECLARE bonus DECIMAL(10, 2);
    SET bonus = salary * 0.10; -- 10% bonus
    RETURN bonus;
END$$

DELIMITER ;
