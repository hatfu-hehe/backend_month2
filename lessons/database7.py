# Databases
# hardcoding
# learn some info about SQL !
# hackerrank SQL - website for solving code sets with SQl requests

# pypi - website for downloading pockets (libraries) for Python
# learn how pockets are made

import sqlite3

def create_tables(conn):
    conn.execute('''DROP TABLE IF EXISTS students''')         # better not to use
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT,
       age INTEGER,
       city TEXT                           
    )
    """)                               # the ',' id not needed if the column is in the end

# C in CRUD stands for Create
# R in CRUD stands for Read
# U in CRUD stands for Update
# D in CRUD stands for Delete
def change_student(conn, name, age, city, student_id):
    conn.execute("""
    UPDATE students 
    SET name = ?, age = ?, city = ?
    WHERE id = ?""",
    (name, age, city, student_id))
    conn.commit()

def add_student(conn, name, age, city):
    # adding data
    conn.execute("""
    INSERT INTO students (name, age, city) VALUES (?, ?, ?)
    """, (name, age, city)
    )
    conn.commit()

def show_students(conn):
    result = conn.execute("SELECT * FROM students")
    # result = conn.execute("SELECT name, age FROM students LIMIT 5")
    return result.fetchall()                   # returns the data in a list with kortezhi
    # return result.fetchmany(20)              # returns the exact number of streams defined in the brackets

def get_student_by_name(conn, name):
    result = conn.execute("""
       SELECT * FROM students
       WHERE name = ?""",
    (name,))
    return result.fetchall()

def get_student_by_id(conn, student_id):
    result = conn.execute("""
       SELECT * FROM students
       WHERE id = ?""",
    (student_id,))
    return result.fetchone()        # returns kortezh

def delete_student(conn, student_id):
    conn.execute("""
       DELETE FROM students
       WHERE id = ?""",
    (student_id,))
    conn.commit()
    # nano, vim

def delete_by_city(conn, city):
    conn.execute("""
        DELETE FROM students
        WHERE city = ?""",
    (city,))
    conn.commit()


if __name__ == "__main__":
    connection = sqlite3.connect('database1.db')

    create_tables(connection)

    add_student(
         connection,
        'Zhong Li',
        '30',
        'Bishkek'
    )

    add_student(
         connection,
        'Aizhamal',
        '19',
        'Bishkek'
    )

    add_student(
         connection,
        'Daniel',
        '19',
        'Novopokrovka'
    )

    add_student(
         connection,
        'Akmaral',
        '19',
        'Kant'
    )

    students = show_students(connection)
    print(students)

    print("=== filtering ===")
    student1 = get_student_by_name(connection, 'Akmaral')
    print(student1)
    student3 = get_student_by_id(connection, 1)
    print(student3)

    print("=== deleting ===")
    delete_student(connection, student_id=1)
    delete_by_city(connection, 'Novopokrovka')
    students = show_students(connection)
    print(students)

    print('=== updating ===')
    change_student(
        connection,
        'Akmaral',
        20,
        'Bishkek',
        4,
    )
    students = show_students(connection)
    print(students)

    connection.close()                # every connection has to be closed at the end