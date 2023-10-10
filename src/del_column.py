import sqlite3

conn = sqlite3.connect('../data/db/all_data.db')

cur = conn.cursor()

cur.execute("ALTER TABLE department_data DROP COLUMN 2023-10-10T011441")

cur.execute("ALTER TABLE department_data DROP COLUMN 2023-10-10T011741")

cur.execute("ALTER TABLE sex_data DROP COLUMN 2023-10-10T011441")

cur.execute("ALTER TABLE sex_data DROP COLUMN 2023-10-10T011741")

cur.execute("ALTER TABLE type_data DROP COLUMN 2023-10-10T011441")

cur.execute("ALTER TABLE type_data DROP COLUMN 2023-10-10T011741")

cur.execute("ALTER TABLE year_data DROP COLUMN 2023-10-10T011441")

cur.execute("ALTER TABLE year_data DROP COLUMN 2023-10-10T011741")

cur.commit()

conn.close()
