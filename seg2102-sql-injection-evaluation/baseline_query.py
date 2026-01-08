# baseline_query.py
# Insecure dynamic SQL construction (vulnerable to SQL Injection)

username = input("Enter username: ")
password = input("Enter password: ")

query = (
    "SELECT * FROM users "
    "WHERE username = '" + username + "' "
    "AND password = '" + password + "'"
)

cursor.execute(query)
0