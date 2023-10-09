import sqlite3

# open db 
conn = sqlite3.connect('../data/db/all_data.db')

# get cursor
cur = conn.cursor()

# get all tables
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

# print all tables
tables = [table[0] for table in cur.fetchall()]

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

print(cur.fetchall())

cur.execute("SELECT * FROM department_data")

print([description[0] for description in cur.description])

print(cur.fetchall())