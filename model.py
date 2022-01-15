import sqlite3
from flask import g


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("db/dap_admin.db")
    return db


def get_projects():
    conn = get_db()
    c = conn.cursor()
    projects_from_db = c.execute("""SELECT uid, project_name,
                    project_db
                    FROM
                    dap_project 
                    ORDER BY uid
    """)
    projects = []
    for row in projects_from_db:
        project = {
            "id": row[0],
            "project": row[1],
            "db": row[2]
        }
        projects.append(project)

    return projects


def get_project_list():
    projects=get_projects()
    list=[]
    for row in projects:
        id=row['id']
        name=row['project']
        list.append((id, name))
    return list


def get_workpack_list():
    workpacks=get_workpacks()
    list=[]
    for row in workpacks:
        id=row['id']
        name=row['workpack']
        list.append((id, name))
    return list


def get_workpacks():
    conn = get_db()
    c = conn.cursor()

    workpacks_from_db = c.execute("""SELECT w.uid as wkp_id, 
                    p.project_name, w.workpack_name, w.workpack_extent
                    FROM
                    dap_project AS p
                    INNER JOIN dap_workpack AS w ON p.uid = w.project_id
                    ORDER BY p.uid
    """)

    workpacks = []
    for row in workpacks_from_db:
        workpack = {
            "id": row[0],
            "project": row[1],
            "workpack": row[2],
            "extent": row[3]
        }
        workpacks.append(workpack)

    return workpacks


def get_workpack_details(wpk_id):
    conn = get_db()
    c = conn.cursor()

    workpack_details_from_db = c.execute("""SELECT wpk.uid as wkp_id, wpk.workpack_name, 
                    user.user_name, user.user_email,
                    role.role_name
                    FROM
                    workpack_user_role AS link_table
                    INNER JOIN dap_workpack AS wpk ON link_table.workpack_id = wpk.uid
                    INNER JOIN dap_user AS user on link_table.user_id = user.uid
                    INNER JOIN dap_role AS role on link_table.role_id = role.uid 
                    WHERE wpk.uid = {}
                    ORDER BY wpk.uid
    """.format(wpk_id))

    workpacks_details = []
    for row in workpack_details_from_db:
        workpack_detail = {
            "id": row[0],
            "workpack": row[1],
            "user": row[2],
            "user_email": row[3],
            "role": row[4]
        }
        workpacks_details.append(workpack_detail)
    return workpacks_details


def get_specific_workpack(id):
    workpacks = get_workpacks()
    for row in workpacks:
        if row['id'] == id:
            return row


def get_specific_workpack_details(id):
    workpacks = get_workpack_details(id)

    return workpacks


def get_users():
    conn = get_db()
    c = conn.cursor()

    users_from_db = c.execute("""SELECT uid, user_name, user_email
                    FROM dap_user
    """)

    users = []
    for row in users_from_db:
        user = {
            "id": row[0],
            "name": row[1],
            "email": row[2]
        }
        users.append(user)

    return users


def get_user_list():
    users=get_users()
    list=[]
    for row in users:
        id=row['id']
        name=row['name']
        list.append((id, name))
    return list


def get_roles():
    conn = get_db()
    c = conn.cursor()

    roles_from_db = c.execute("""SELECT uid, role_name, role_level
                    FROM dap_role
    """)
    roles = []
    for row in roles_from_db:
        role = {
            "id": row[0],
            "name": row[1],
            "level": row[2]
        }
        roles.append(role)

    return roles    


def get_role_list():
    roles=get_roles()
    list=[]
    for row in roles:
        id=row['id']
        name=row['name']
        list.append((id, name))
    return list    

