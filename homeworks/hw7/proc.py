 # Create the stored procedure
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",  # Change to your host
    user="root",       # Your MySQL username
    password="123"  # Your MySQL password
)

cursor = conn.cursor()

procedure_query = """
DELIMITER $$

CREATE PROCEDURE update_salary(
    IN emp_id INT,
    IN increment DECIMAL(10, 2)
)
BEGIN
    UPDATE employees
    SET salary = salary + increment
    WHERE id = emp_id;
END$$

DELIMITER ;
"""

cursor.execute(procedure_query, multi=True)
print("Procedure created!")

# Call the procedure
cursor.callproc("update_salary", (1, 5000))  # Increment salary of employee with ID 1
conn.commit()
print("Salary updated!")
