import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/dap_admin.db'

os.remove(db_abs_path)

conn = sqlite3.connect(db_abs_path)
cursor = conn.cursor()

sql_file = open("../resources/sqlite/dap_admin_sqlite_create.sql")
sql_as_string = sql_file. read()

cursor.executescript(sql_as_string)
print("Created ")

sql_file = open("../resources/sqlite/dap_admin_sqlite_insert.sql")
sql_as_string = sql_file. read()

cursor.executescript(sql_as_string)
print("Inserted ")
