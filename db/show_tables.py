import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/dap_admin.db'

print("Options: (all, project, workpack, user, roles, workpack_user_role)")
table = input("Show table: ")

conn = sqlite3.connect(db_abs_path)
cursor = conn.cursor()


def show_projects():
    try:
        print ("projects")
        for row in cursor.execute("SELECT * FROM dap_project"):
            print(row)
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

def show_workpacks():
    try:
        print("workpack")
        for row in cursor.execute("SELECT * FROM dap_workpack"):
            print(row)
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

def show_users():
    try:
        print("user")
        for row in cursor.execute("SELECT * FROM dap_user"):
            print(row)
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

def show_roles():
    try:
        print("role")
        for row in cursor.execute("SELECT * FROM dap_role"):
            print(row)
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

def show_workpack_user_roles():
    try:
        print("workpack_user_roles")
        for row in cursor.execute("SELECT * FROM workpack_user_role"):
            print(row)
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

if table == "project":
    show_projects()
elif table == "workpack":
    show_workpacks()
elif table == "user":
    show_users()
elif table == "role":
    show_roles()
elif table == "subcategories":
    show_workpack_user_roles()
elif table == "all":
    show_projects()
    show_workpacks()
    show_users()
    show_roles()
    show_workpack_user_roles()
else:
    print("This option does not exist.")

conn.close()
