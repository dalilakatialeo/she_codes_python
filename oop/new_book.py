import sqlite3


#connect to SQLite = opens a connection to the SQLite database file, books.db
connection = sqlite3.connect("books.db") #.db signifies the file is a database


# create a cursor object, used to invoke methods that execute SQl, fetch data from query results
cursor = connection.cursor()

# create a table then populate with data
# arbitrary, but using upper case highlights key words


#execute an sql statement
cursor.execute("""
    DROP TABLE IF EXISTS books
""")

cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,     
        title TEXT, 
        pages INTEGER,
        current_page INTEGER
    )
""")

cursor.execute("""
INSERT INTO books VALUES (
    0, "A great book", 213, 27
    )
""")

cursor.execute("""
INSERT INTO books VALUES (
    1, "Another great book", 395, 387
    )
""")

rows = cursor.execute("""
    SELECT title FROM books WHERE title="A great book"
""")

def calculate_read_time():
    read_speed = input("How many pages do you read per minute?")
    for row in rows:
        read_time = row[2] / float(read_speed) / 60
        print("Book:", row)
        print("%.2f" % read_time, "hours to read", row[1])
        
calculate_read_time()

# cursor.execute("""
#     DELETE FROM books WHERE id=0 (
# """)

cursor.execute("""
    UPDATE books SET current_page= 100 WHERE id=1
""")
connection.commit()

connection.close()
