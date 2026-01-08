# prepared_statement.py
# Secure SQL query using prepared statements (parameterized query)

username = input("Enter username: ")
password = input("Enter password: ")

query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
