import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()
cursor.execute(
    """
SELECT STUDENTS.name, GRADES.course_id, GRADES.grade
FROM STUDENTS
JOIN GRADES ON STUDENTS.id = GRADES.student_id
"""
)
for row in cursor.fetchall():
    print(row)
conn.close()
