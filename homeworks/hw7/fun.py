# example of func used
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",  # Change to your host
    user="root",       # Your MySQL username
    password="123"  # Your MySQL password
)

cursor = conn.cursor()
# Insert sample data
cursor.execute("INSERT INTO employees (name, salary, department) VALUES (%s, %s, %s)", 
               ("Alice", 50000, "HR"))
cursor.execute("INSERT INTO employees (name, salary, department) VALUES (%s, %s, %s)", 
               ("Bob", 60000, "Engineering"))
conn.commit()

# Call the function for a specific salary
cursor.execute("SELECT calculate_bonus(salary) FROM employees WHERE name = %s", ("Alice",))
bonus = cursor.fetchone()[0]
print(f"Alice's bonus: {bonus}")
