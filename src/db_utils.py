import sqlite3
import os

def save_to_db(data, date_generated):
    # we're going to have a separate table for different sets of data:
    # societies, departments, year, type (UG, PGR, PGT)

    db_file_path = "../data/db/all_data.db"

    if not os.path.exists(db_file_path):
        print("[ERROR] Database file does not exist. A new one will be created...")

    conn = sqlite3.connect(db_file_path)
    cur = conn.cursor()

    tables = ["department_data", "sex_data", "year_data", "type_data"]

    for table in tables:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='" + table + "'")

        if cur.fetchone() is None:
            print("[ERROR] Table " + table + " does not exist. Creating it now...")
            cur.execute("CREATE TABLE " + table + " (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, votes INTEGER, eligible INTEGER, date_generated TEXT)")            


    for dataset in data["Groups"]:
        if "Department" in dataset["Name"]:
            table_name = "department_data"

            cur.execute("SELECT name FROM " + table_name)
            deps_in_db = [dep[0] for dep in cur.fetchall()]

            deps = {}
            for dep in dataset["Items"]:
                deps[dep["Name"]] = (dep["Voters"], dep["Eligible"])
            
            cur.execute("SELECT * FROM " + table_name)

            print("Current data in database: ")

            for dep in deps:
                if dep not in deps_in_db:
                    print("[INFO] Inserting " + dep + " into database...")
                    command = "UPDATE " + table_name + " SET votes = " + str(deps[dep][0]) + ", eligible = " + str(deps[dep][1]) + ", date_generated = '" + date_generated + "' WHERE name = '" + dep + "'"
                    print(command)
                    try:
                        cur.execute(command)
                    except Exception as e:
                        print("[ERROR] Could not insert data into database: " + str(e))
                else:
                    print("[INFO] Updating " + dep + " in database...")
                    command = "INSERT INTO " + table_name + " (name, votes, eligible, date_generated) VALUES ('" + dep + "', " + str(deps[dep][0]) + ", " + str(deps[dep][1]) + ", '" + date_generated + "')"
                    try:
                        cur.execute(command)
                    except Exception as e:
                        print("[ERROR] Could not insert data into database: " + str(e))


        elif "Year of study" in dataset["Name"]:
            table_name = "year_data"
            pass




        elif "Student type" in dataset["Name"]:
            table_name = "type_data"
            pass




        elif "Sex" in dataset["Name"]:
            table_name = "sex_data"
            pass


    conn.commit()

    cur.execute("SELECT * FROM department_data")

    print(cur.fetchall())

    conn.close()







