import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS STUDENTS (
    id INTEGER PRIMARY KEY,
    name TEXT
)
"""
)
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS GRADES (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id TEXT,
    grade INTEGER,
    FOREIGN KEY(student_id) REFERENCES STUDENTS(id)
)
"""
)
conn.commit()
conn.close()
print("Οι πίνακες STUDENTS και GRADES δημιουργήθηκαν.")
