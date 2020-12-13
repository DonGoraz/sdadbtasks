from databases import DatabaseContextManager, DATABASE_FILE


# Part 1: Task 1,2
def create_employees():
    query = """CREATE TABLE IF NOT EXISTS EmployeeĮ(
                employeeId INTEGER PRIMARY KEY AUTOINCREMENT,
                firstName VARCHAR ,
                lastName VARCHAR ,
                dateOfBirth DATE)"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)
create_employees()

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





