from databases import DatabaseContextManager, DATABASE_FILE
from objects.employees import Employee


# Part 2 Task 1
def create_employee(employee):
    query = '''INSERT INTO Employees(firstName, lastName, dateOfBirth, phoneNumber, email, salary) 
                VALUES (?,?,?,?,?,?)'''
    params = [employee.first_name, employee.last_name, employee.date_of_birth, employee.phone_number, employee.email,
              employee.salary]
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, params)

employee1 = Employee('''Hel"lo's''', 'Johnson', '1975-01-01', '0-800-800-314', 'john@johnson.com', 1000)
employee2 = Employee('James', 'Jameson', '1985-02-02', '0-800-800-999', 'james@jameson.com', 2000)
employee_list = [employee1,employee2]

# Part 2 Task 2
def update_date_of_birth(employee, new_date):
    query = """UPDATE Employees
                SET dateOfBirth = ?
                WHERE firstName = ? AND lastName = 1980"""
    params = [new_date, employee.first_name, employee.last_name]
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, params)
    employee.date_of_birth = new_date

# update_date_of_birth(employee1, '1980-01-01')

# Part 2 Task 3
def delete_everything_from_employees_table():
    query = """DELETE FROM Employees"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)

# delete_everything_from_employees_table()


# Part 2 Task 4
for i in employee_list:
    create_employee(i)


print('''Who's ther"e who lives there''')








