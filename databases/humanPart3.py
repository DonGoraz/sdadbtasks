from databases import DatabaseContextManager, DATABASE_FILE


# Part 3 Task 1
def get_from_employees_table():
    query = """SELECT * FROM Employees"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)
        for i in cursor:
            print(i)
# Part 3 Task 2

get_from_employees_table()



