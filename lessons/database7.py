# Databases
# hardcoding

import sqlite3

def create_tables(conn):
    conn.execute('''DROP TABLE IF EXISTS students''')         # better not to use
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
       name TEXT,
       age INTEGER,
       city TEXT                           
    )
    """)                               # the ',' id not needed if the column is in the end

def add_student(conn, name, age, city):
    # adding data
    conn.execute("""
    INSERT INTO students VALUES (?, ?, ?)
    """, (name, age, city)
                 )
    conn.commit()

def show_students(conn):
    result = conn.execute("SELECT * FROM students")
    return result.fetchall()

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
        'Akmaral',
        '19',
        'Kant'
    )

    students = show_students(connection)
    print(students)

    connection.close()                # every connection has to be closed at the end