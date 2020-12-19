from databases.humansDatabaseTask import DatabaseContextManager, DATABASE_FILE

# Part 3:
# 1.Select everything from tableemployees.
# 2.Select only firstName and lastName from tableemployees.
# 3.Select all employees with lastName Johnson.
# 4.Select all employees whose lastName starts with J.
# 5.Select all employees whose lastName contains so.
# 6.Select all employees born after 1980.
# 7.Select all employees born after 1980 and whose firstName is John.
# 8.Select all employees born after 1980 or whose firstName is John.
# 9.Select all employees whose lastName is not Jameson.
# 10.Select maximum salary.
# 11.Select minimum salary.
# 12.Select average salary

# Part 3 Task 1
def get_from_employees_table():
    query = """SELECT * FROM Employees"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)
        for i in cursor:
            print(i)

# Part 3 Task 2
def get_first_last_name_employees_table():
    query = """SELECT firstName, lastName FROM Employees"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)
        for i in cursor:
            print(i)

# Part 3 Task 3
def get_employee_by_name_employees_table(name):
    query = """SELECT * FROM Employees
                WHERE lastName = ?"""
    params = [name]
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, params)
        for i in cursor:
            print(i)

# Part 3 Task 4
def get_employee_by_last_name_letters_table(name):
    query = """SELECT * FROM Employees
                WHERE lastName LIKE ?"""
    name = name + "%"
    params = [name]
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, params)
        for i in cursor:
            print(i)

# get_employee_by_last_name_letters_table("J")

# Part 3 Task 5
def get_employee_if_characters_contained_in_table(characters):
    query = """SELECT * FROM Employees
                WHERE lastName LIKE ?"""
    characters = "%" + characters + "%"
    params = [characters]
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, params)
        for i in cursor:
            print(i)

# get_employee_if_characters_contained_in_table("so")

# Part 3 Task 6
def get_employees_after_year_table(year):
    query = """SELECT * FROM Employees
                WHERE dateOfBirth >= ?"""
    year = year
    params = [year]
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, params)
        for i in cursor:
            print(i)

get_employees_after_year_table("1980-01-01")

# Part 3 Task 6
def get_employees_after_year_table(year):
    query = """SELECT * FROM Employees
                WHERE dateOfBirth >= ?"""
    year = year
    params = [year]
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, params)
        for i in cursor:
            print(i)

get_employees_after_year_table("1980-01-01")

# Part 3 Task 7
def get_employees_after_year_and_name_table(year, first_name):
    query = """SELECT * FROM Employees
                WHERE dateOfBirth >= ? AND firstName = ?"""
    converted_year_to_fit_db_structure = year + "-01-01"
    params = [converted_year_to_fit_db_structure, first_name]
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, params)
        for i in cursor:
            print(i)

get_employees_after_year_and_name_table("1980", "John")


# Part 3 Task 8
def get_employees_before_year_or_firstname_table(year, first_name):
    query = """SELECT * FROM Employees
                WHERE dateOfBirth >= ? OR firstName = ?"""
    converted_year_to_fit_db_structure = year + "-01-01"
    params = [converted_year_to_fit_db_structure, first_name]
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, params)
        for i in cursor:
            print(i)

get_employees_before_year_or_firstname_table("1980", "John")


# Part 3 Task 9
def get_employees_whose_not_lastname(last_name):
    query = """SELECT * FROM Employees
                WHERE lastName != ?"""
    params = [last_name]
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, params)
        for i in cursor:
            print(i)

get_employees_whose_not_lastname("Jameson")


# Part 3 Task 10
def get_employees_max_salary():
    query = """SELECT MAX(salary) FROM Employees"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)
        for i in cursor:
            print(i)



# Part 3 Task 11
def get_employees_min_salary():
    query = """SELECT MIN(salary) FROM Employees"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)
        for i in cursor:
            print(i)


# Part 3 Task 12
def get_employees_avg_salary():
    query = """SELECT AVG(salary) FROM Employees"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)
        for i in cursor:
            print(i)


get_employees_avg_salary()
