# i have no task in teams but i worked with mysql db so here i just want to show understanding of main concepts 


import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",  # Change to your host
    user="root",       # Your MySQL username
    password="123"  # Your MySQL password
)

cursor = conn.cursor()

# Create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS sample_db")
print("Database created!")

# Select the database
conn.database = "sample_db"

# Create a sample table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    salary DECIMAL(10, 2),
    department VARCHAR(50)
)
""")
print("Table created!")


# to get data

# Fetch and display data
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
