import sqlite3

def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books (
       name TEXT,
       author TEXT,
       publication_year INTEGER,
       genre TEXT,
       number_of_pages INTEGER,
       number_of_copies INTEGER                          
    )
    """)

def insert_books(conn, name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute("""
    INSERT INTO books (name, author, publication_year, genre,
     number_of_pages, number_of_copies) VALUES (?, ?, ?, ?, ?, ?)
    """, (name, author, publication_year, genre, number_of_pages, number_of_copies)
    )
    conn.commit()

def show_library(conn):
    result = conn.execute("SELECT * FROM books")
    return result.fetchall()

if __name__ == "__main__":
    connection = sqlite3.connect('database_hw7.db')

    create_tables(connection)

insert_books(
    connection,
    'Jane Eyre',
    'Charlotte Bronte',
    1847,
    'Novel',
    624,
    18
)

insert_books(
    connection,
    'Pride and Prejudice',
    'Jane Austen',
    1813,
    'Novel',
    432,
    22
)

insert_books(
    connection,
    'The Great Gatsby',
    'F. Scott Fitzgerald',
    1925,
    'Novel',
    180,
    15
)

insert_books(
    connection,
    'To Kill a Mockingbird',
    'Harper Lee',
    1960,
    'Novel',
    336,
    20
)

insert_books(
    connection,
    '1984',
    'George Orwell',
    1949,
    'Dystopia',
    328,
    25
)

insert_books(
    connection,
    'Crime and Punishment',
    'Fyodor Dostoevsky',
    1866,
    'Novel',
    671,
    12
)

insert_books(
    connection,
    'The Master and Margarita',
    'Mikhail Bulgakov',
    1967,
    'Fantasy',
    480,
    17
)

insert_books(
    connection,
    'Don Quixote',
    'Miguel de Cervantes',
    1605,
    'Novel',
    1072,
    8
)

insert_books(
    connection,
    'Brave New World',
    'Aldous Huxley',
    1932,
    'Dystopia',
    311,
    14
)

insert_books(
    connection,
    'The Little Prince',
    'Antoine de Saint-Exupéry',
    1943,
    'Fable',
    96,
    30
)

library = show_library(connection)
print(library)





