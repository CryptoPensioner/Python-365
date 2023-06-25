import sqlite3

conn = sqlite3.connect('data2.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE students (id INTEGER, name TEXT, grade REAL)")
cursor.execute("INSERT INTO students VALUES (1, 'Alice', 99.5)")
cursor.execute("INSERT INTO students VALUES (2, 'Bob', 95.5)")
cursor.execute("INSERT INTO students VALUES (3, 'Charlie', 90.5)")
cursor.execute("INSERT INTO students VALUES (4, 'Diane', 85.5)")
cursor.execute("INSERT INTO students VALUES (5, 'Eve', 99.9)")

conn.commit()

def get_highest_grade():
    cursor.execute("SELECT * FROM students ORDER BY grade DESC LIMIT 1")
    return cursor.fetchone()

print(get_highest_grade())

conn.close()
