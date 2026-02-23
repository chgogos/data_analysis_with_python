import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()
cursor.execute(
    """UPDATE GRADES SET grade = ? 
WHERE student_id = ? AND course_id = ?""",
    (97, 1, "CS101"),
)
conn.commit()
conn.close()
print("Η εγγραφή βαθμολογίας ενημερώθηκε.")
