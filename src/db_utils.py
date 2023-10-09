import sqlite3
import os

def save_to_db(data, date_generated):
    # we're going to have a separate table for different sets of data:
    # societies, departments, year, type (UG, PGR, PGT)

    db_file_path = "../data/db/all_data.db"

    if not os.path.exists(db_file_path):
        print("[ERROR] Database file does not exist.")
        exit()

    conn = sqlite3.connect(db_file_path)
    cur = conn.cursor()

    tables = ["department_data", "society_data", "year_data", "type_data"]

    for table in tables:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='" + table + "'")

        if cur.fetchone() is None:
            print("[ERROR] Table " + table + " does not exist. Creating it now...")
            cur.execute("CREATE TABLE " + table + " (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, votes INTEGER, date_generated TEXT)")
            


    for dataset in data["Groups"]:
        if "Department" in dataset["Name"]:
            table_name = "department_data"




        elif "All Societies" in dataset["Name"]:
            table_name = "society_data"




        elif "Year of study" in dataset["Name"]:
            table_name = "year_data"




        elif "Student type" in dataset["Name"]:
            table_name = "type_data"




