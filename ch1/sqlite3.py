import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO STUDENTS (name) VALUES (?)", ("Αντώνης",))
cursor.execute(
    "INSERT INTO GRADES (student_id, course_id, grade) VALUES (?, ?, ?)",
    (1, "CS101", 95),
)
cursor.execute(
    "INSERT INTO GRADES (student_id, course_id, grade) VALUES (?, ?, ?)",
    (1, "CS102", 88),
)
conn.commit()
conn.close()
print("Εισήχθησαν εγγραφές στους πίνακες STUDENTS και GRADES.")
