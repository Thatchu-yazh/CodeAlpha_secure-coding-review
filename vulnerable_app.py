import sqlite3

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "admin123"

# Database connection
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")

# User input
username = input("Enter username: ")
password = input("Enter password: ")

# Vulnerable SQL query (SQL Injection)
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

print("\nExecuting Query:")
print(query)

cursor.execute(query)

result = cursor.fetchall()

if result:
    print("Login Successful")
else:
    print("Invalid Credentials")

conn.close()