import sqlite3

# open db 
conn = sqlite3.connect('../data/db/all_data.db')

# get cursor
cur = conn.cursor()

# get all tables
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

# print all tables
tables = [table[0] for table in cur.fetchall()]

for table in tables:
    print("Table: " + table)
    cur.execute("SELECT * FROM " + table)
    for row in cur.fetchall():
        print(row)