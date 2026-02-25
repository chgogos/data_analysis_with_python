try:
    filename = input("Δώσε όνομα αρχείου: ")
    f = open(filename, "r")
    content = f.read()
    print("Το αρχείο διαβάστηκε επιτυχώς.")
    f.close()
except FileNotFoundError:
    print("Σφάλμα: Το αρχείο δεν βρέθηκε.")
except PermissionError:
    print("Σφάλμα: Δεν υπάρχουν δικαιώματα πρόσβασης στο αρχείο.")
else:
    print("Η ανάγνωση ολοκληρώθηκε χωρίς σφάλματα.")
finally:
    print("Τέλος διαδικασίας.")
