from databases.humansDatabaseTask import DatabaseContextManager, DATABASE_FILE
from objects.employees import Employee

# 1.Alter table employees:a.make employeeId column PRIMARY KEY, NOT NULL and AUTO INCREMENT.
# 2.See what happens when you add two more entries in employees, this time without setting the employeeId manually:
#     a.'Julie', 'Juliette', '1990-01-01', '0-800-900-111', 'julie@juliette.com', 5000
#     b.'Sofie', 'Sophia', '1987-02-03', '0-800-900-222', 'sofie@sophia.com', 1700
# 3.Create a new table departments, with columns:
#     a.departmentId - Integer, PRIMARY KEY, NOT NULL, AUTO INCREMENT
#     b.name - Varchar, NOT NULL
# 4.Add two entries in table departments:
#     a.HR,
#     b.Finance.
# 5.Connect the two tables together - employees should have a reference to departments:
#     a.add departmentId - Integer column to employees table,
#     b.assign John to HR and Julie to Finance.
# 6.Delete entry HR from departments table:
#     a.Does this work?
#     b.Should we be able to delete it? If John is assigned to HR and we delete, is the data still correct?
# 7.Create a foreign key in employees table to departments table:
#     a.departmentId column in employees should reference departmentId column in departments,
#     b.remember the naming convention: fk_employees_departments.
# 8.Now try to delete entry HR from departments table:
#     a.Does this still work?
# 9.Now try to add a new employee and set its departmentId to 10:
#         a.Does this work? Should it?
#         b.Try to add this new employee and set its departmentId to 1. Does this work?
# 10.Try deleting the newly added employee:
#         a.Does it work? Should it?

employee1 = Employee('Julie', 'Juliette', '1990-01-01', '0-800-900-111', 'julie@juliette.com', 5000)
employee2 = Employee('Sofie', 'Sophia', '1987-02-03', '0-800-900-222', 'sofie@sophia.com', 1700)
employee_list = [employee1, employee2]


# Parses the list of employee objects and makes them into a list. (removes id values as database sets id itself)
def function_parse_employee_objects_into_lists(employee_list):
    data_normalization = []
    for employees in employee_list:
        employee_info = []
        for k, v in employees.__dict__.items():
            if k == "id":
                continue
            employee_info.append(v)
        data_normalization.append(employee_info)
    return data_normalization

# Part 4 Task1
# Can't do this task in SQLITE

# Part 4 Task 2
def part4_task2(employee_list):
    query = """INSERT INTO EMPLOYEES(firstName, lastName,dateOfBirth,phoneNumber,email,salary) VALUES (?,?,?,?,?,?)"""
    normalized_data = function_parse_employee_objects_into_lists(employee_list)
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.executemany(query, normalized_data)

# Call this method to write from a object list of users into database.
# part4_task2(employee_list)


# Part 4: Task 3
def part4_task3():
    query = """CREATE TABLE IF NOT EXISTS Departments(
                departmentId INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR NOT NULL)"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)

# Part 4 Task 4
def part4_task4(depart_name):
    query = """INSERT INTO Departments(name) VALUES (?)"""
    params = (depart_name,)
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, params)

# Part 4 Task 5
update_info = [[6,"John"],[2,"Julie"]]
def part4_task5(list):
    query = """UPDATE Employees
                SET departmentId = ?
                WHERE firstName = ?"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.executemany(query, list)

# Part 4 Task 6
def part4_task6(name):
    query = """DELETE FROM Departments
                WHERE name = ?"""
    params = (name,)
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, params)


# Part 4 Task 7
# SQLITE can't do this. The solution is in Part1 Task1 you have to initially create foreign key on table creation

# Part 4 Task 8
# Still works does the same as Part 4 Task 6 But SQLITE doesn't have the right functionality to support the restrictions of deletion.

# Part 4 Task 9
# Still works because of SQLITE implementation

# Part 4 Task 10
# In SQLITE you can delete anything you want as it doesn't prohibit deletion even if foreign keys are set.