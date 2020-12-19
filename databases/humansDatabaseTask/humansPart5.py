from databases.humansDatabaseTask import DatabaseContextManager, DATABASE_FILE
# Part 5:
# 1.Identify the type of relationship between employees and departments tables.
# 2.Add additional functionality to the employees table by allowing a specific employee to have a manager.
# How would you model this considering the fact that the manager should also be an employee?
# 3.Make Sophie the manager of John and James.
# 4.Add additional functionality:
# a.database will store project information as well, projectId and description,
# b.design the database in such a way that an employee will be able to work on multiple projects and also multiple employees can work on the same project.
# 5.Insert two projects to the database:a.Python - Cinema Web App,b.Java - Fitness Web App.
# 6.Assign John and James to the Python project and Julie and Sofie to the Java project


# Part 5 Task 1:
# employees many - departments one (many to one)

# PART 5 Task 2:
# Can't do it in SQLITE but solved this by adding managerId in Part1_Task1

# PART 5 Task 3
update_info = [[4,"John"],[4,"James"]]
def part5_task3(list):
    query = """UPDATE Employees
                SET managerId = ?
                WHERE firstName = ?"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.executemany(query, list)
part5_task3(update_info)



# PART 5 Task 4
def part5_task4():
    query = """CREATE TABLE IF NOT EXISTS Projects(
                projectId INTEGER PRIMARY KEY AUTOINCREMENT,
                description varchar(255) DEFAULT NULL)"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)

# PART 5 Task 4b
def part5_task5():
    query = """CREATE TABLE IF NOT EXISTS EmployeesProjects(
  employeeProjectId INTEGER PRIMARY KEY AUTOINCREMENT,
  employeeId INTEGER NOT NULL,
  projectId INTEGER NOT NULL,
  FOREIGN KEY (employeeId) REFERENCES Employees(employeeId),
  FOREIGN KEY (projectId) REFERENCES Projects(projectId))"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)

# PART 5 Task 5
list_of_projects = [('Python - Cinema Web App',),('Java - Fitness Web App',),('Testing - Human Resources App',)]
def part5_task5(project_list):
    query = """INSERT INTO Projects(description) VALUES (?)"""

    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.executemany(query, project_list)

# PART 5 Task 6
list_of_employee_project_connections = [(1,1),(2,1),(3,2),(4,2)]
def part5_task6(project_employee_connections):
    query = """INSERT INTO EmployeesProjects(employeeId, projectId) VALUES (?,?)"""

    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.executemany(query, project_employee_connections)

part5_task6(list_of_employee_project_connections)