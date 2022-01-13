CREATE TABLE dap_project (
	uid integer PRIMARY KEY AUTOINCREMENT,
	project_name text,
	project_db text
);

CREATE TABLE dap_workpack (
	uid integer PRIMARY KEY AUTOINCREMENT,
	workpack_name text,
	project_id integer,
	workpack_extent text
);

CREATE TABLE dap_user (
	uid integer PRIMARY KEY AUTOINCREMENT,
	user_name text,
	user_email text
);

CREATE TABLE dap_role (
	uid integer PRIMARY KEY AUTOINCREMENT,
	role_name text,
	role_level integer
);

CREATE TABLE workpack_user_role (
	uid integer PRIMARY KEY AUTOINCREMENT,
	workpack_id integer,
	user_id integer,
	role_id integer
);






