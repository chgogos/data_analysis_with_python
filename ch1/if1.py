grade = int(input("Εισάγετε βαθμό (0-20): "))

if grade < 0 or grade > 20:
    print("Μη έγκυρη τιμή βαθμού")
elif grade < 10:
    print("Αποτυχία")
elif grade < 18:
    print("Επιτυχία")
else:
    print("Άριστα")