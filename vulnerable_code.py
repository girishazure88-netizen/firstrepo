# Sample Vulnerable Python Code

# This code demonstrates an example of SQL Injection, a common security issue.
import sqlite3

def get_user_data(username):
    # Vulnerable to SQL Injection
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username='{username}'")
    return cursor.fetchall()

# Example of usage
user_input = "'; DROP TABLE users; --"
print(get_user_data(user_input))
