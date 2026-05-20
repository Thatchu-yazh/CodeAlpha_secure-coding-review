import sqlite3
import hashlib

# Database connection
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")

# User input
username = input("Enter username: ")
password = input("Enter password: ")

# Hash the password
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# Secure parameterized query
query = "SELECT * FROM users WHERE username=? AND password=?"

cursor.execute(query, (username, hashed_password))

result = cursor.fetchall()

if result:
    print("Login Successful")
else:
    print("Invalid Credentials")

conn.close()
