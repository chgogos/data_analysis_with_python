try:
    x = int(input("Δώσε έναν ακέραιο: "))
    y = 1 / x
    print("Αποτέλεσμα:", y)
except ZeroDivisionError:
    print("Σφάλμα: Διαίρεση με το μηδέν.")
except ValueError:
    print("Σφάλμα: Μη έγκυρη αριθμητική είσοδος.")
except Exception:
    print("Γενικό σφάλμα που ανήκει στην ιεραρχία της Exception.")
finally:
    print("Τέλος εκτέλεσης.")
