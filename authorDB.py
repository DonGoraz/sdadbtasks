from databases import DatabaseContextManager

DATABASE_FILE = "Database"


def create_author_table():
    query = """CREATE TABLE IF NOT EXISTS Authors(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                last_name TEXT,
                birth_year DATE)"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)


create_author_table()


def create_author(name: str, last_name: str, birth_year):
    query = """INSERT INTO Authors(name, last_name, birth_year) VALUES (?,?,?)"""  # formats of ? in other engines: %, s%
    params = (name, last_name, birth_year)

    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, params)


def get_author():
    query = """SELECT * FROM Authors"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)
        print(cursor.fetchall())


# def update_book(new_title, old_title):
#     query = """UPDATE Authors
#                 SET title=?
#                 WHERE title=?"""
#     parameters = (new_title, old_title)
#     with DatabaseContextManager(DATABASE_FILE) as cursor:
#         cursor.execute(query, parameters)


# def delete_book(book_id):
#     query = """DELETE FROM Books
#                 Where id=?"""
#     parameters = (book_id,)
#     with DatabaseContextManager(DATABASE_FILE) as cursor:
#         cursor.execute(query, parameters)

    # create_book_table()
    #
    # book_title = "jo2655hn j4than"
    # description = "nesvarbu"
    # create_book(book_title, description)
    # update_book("whatever", "doesntmatter")
    # delete_book(4)
    # get_book()


create_author_table()
create_author("john", "johnathan", '2020-00-00')
get_author()