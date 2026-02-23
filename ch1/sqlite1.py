import sqlite3

conn = sqlite3.connect("school.db")
print("Η Βάση Δεδομένων δημιουργήθηκε και συνδέθηκε.")
conn.close()
