from databases import DatabaseContextManager, DATABASE_FILE

DATABASE_FILE = "Database"


def create_book_table():
    query = """CREATE TABLE IF NOT EXISTS Post(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                post_text TEXT UNIQUE,
                author_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES Authors(id) ON DELETE CASCADE)"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)



def create_book(title: str, description: str, author_id):
    query = """INSERT INTO Books(title, description, author_id) VALUES (?,?,?)"""  # formats of ? in other engines: %, s%
    params = (title, description, author_id)
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, params)


def get_book():
    query = """SELECT * FROM Books"""
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, )
        print(cursor.fetchall())


def update_book(new_title, old_title):
    query = """UPDATE Books
                SET title=?
                WHERE title=?"""
    parameters = (new_title, old_title)
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, parameters)


def delete_id_section(floor_range, ceiling_range):
    query = """DELETE FROM Books
                WHERE id BETWEEN ? AND ?"""
    parameters = (floor_range, ceiling_range)
    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query, parameters)


def book_author_join():
    query = """SELECT COUNT(Books.id),title,description, birth_year, Authors.id FROM Books
                JOIN Authors
                    ON Authors.id = Books.author_id
                GROUP BY Authors.id"""

    with DatabaseContextManager(DATABASE_FILE) as cursor:
        cursor.execute(query)
        for i in cursor.fetchall():
            print(i)


# def book_author_foreignkey():
#     query = """DROP TABLE Books"""
#     with DatabaseContextManager(DATABASE_FILE) as cursor:
#         cursor.execute(query,)


create_book_table()

book_title = "532152 523152"
description = "fd23f32"
author_id = 8

# create_book(book_title, description, author_id)
# update_book("whatever", "doesntmatter")
# delete_id_section(3,7)
# get_book()

book_author_join()


