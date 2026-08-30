import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

username = input("Enter username: ")
password = input("Enter password: ")

password_hash = hash_password(password)

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username = ? AND password = ?"

cursor.execute(query, (username, password_hash))

result = cursor.fetchone()

if result:
    print("Login successful")
else:
    print("Invalid username or password")

conn.close()
