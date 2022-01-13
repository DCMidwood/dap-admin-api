INSERT INTO dap_project
VALUES
    (1, "ProjectA", "dbA"),
    (2, "ProjectB", "dbB");


INSERT INTO dap_workpack
VALUES
	(1, "WorkpackAlpha", "1", "39.77,-86.15"),
    (2, "WorkpackBeta", "1", "40,-79.9"),
    (3, "WorkpackCharlie", "2","40.565,-120.5959"),
    (4, "WorkpackDelta", "2","40.565,-3.5959");


INSERT INTO dap_user
VALUES
    (1, "Daniel", "daniel@mail.com"),
    (2, "Carlos", "daniel@mail.com");

	
INSERT INTO dap_role
VALUES
    (1, "GIS", 3),
    (2, "Admin", 1),
	(3, "Engineer", 3),
    (4, "Checker", 2);


INSERT INTO workpack_user_role
VALUES
	(1, 1, 1, 3),
    (2, 1, 2, 2),
    (3, 1, 1, 2),
	(4, 2, 2, 3);







