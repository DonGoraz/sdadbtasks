from databases.humansDatabaseTask import DatabaseContextManager, DATABASE_FILE

# 1.Create a new database: humanResources.
# 2.Create a new table employees, with the following columns:
# a.employeeId - Integer,b.firstName - Varchar,c.lastName - Varchar,d.dateOfBirth - Date,e.postalAddress - Varchar.
# 3.Alter table employees and add the following columns:
# a.phoneNumber - Varchar,b.email - Varchar,c.salary - Integer.
# 4.Alter table employees and remove the postalAddress column.
# 5.Create a new table employeeAddresses, with country - Varchar column.
# 6.Remove table employeeAddresses


# Part 1: Task 1,2
def create_employees():
    query = """CREATE TABLE IF NOT EXISTS Employees(
                employeeId INTEGER PRIMARY KEY AUTOINCREMENT,
                firstName VARCHAR ,
                lastName VARCHAR ,
                dateOfBirth DATE,
                phoneNumber TEXT,
                email TEXT,
                salary INTEGER,
                departmentId INTEGER,
                managerId INTEGER,
                FOREIGN KEY (managerId) REFERENCES Employees(employeeId),
                FOREIGN KEY (departmentId) REFERENCES Departments(departmentId))"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)

# Part 1: Task 3
def alter_employees():
    query = """ALTER TABLE Employees
                ADD salary INTEGER"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)

# Skip task 4 as sqlite doesn't have functionality for that.

# Part 1: Task 5
def create_employee_address_table():
    query = """CREATE TABLE IF NOT EXISTS EmployeesAddresses(
                country VARCHAR )
                """
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)

# Part 1: Task 6
def delete_employee_address_table():
    query = """DROP Table EmployeesAddresses
                """
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)






