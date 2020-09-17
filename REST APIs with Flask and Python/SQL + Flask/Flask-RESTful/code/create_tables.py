import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# id defined like this means that it will be auto incrementing and we do not need to specify it when creating users
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)" # real - float
cursor.execute(create_table)

connection.commit()

connection.close()
