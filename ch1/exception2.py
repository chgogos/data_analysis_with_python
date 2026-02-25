class NoPositiveNumbersError(Exception):
    """Εξαίρεση που εγείρεται όταν δεν υπάρχουν θετικοί αριθμοί."""
    pass


def average_positive(numbers):
    if not numbers:
        raise ValueError("Η λίστα είναι κενή.")
    positive_nums = [x for x in numbers if x > 0]
    if not positive_nums:
        raise NoPositiveNumbersError(
            "Δεν υπάρχουν θετικοί αριθμοί για υπολογισμό μέσου όρου."
        )
    return sum(positive_nums) / len(positive_nums)


try:
    data = list(map(int, input("Δώσε ακέραιους χωρισμένους με κενό: ").split()))
    avg = average_positive(data)
    print("Μέσος όρος θετικών αριθμών:", avg)
except ValueError as e:
    print("Σφάλμα εισόδου:", e)
except NoPositiveNumbersError as e:
    print("Προσαρμοσμένη εξαίρεση:", e)
finally:
    print("Τέλος εκτέλεσης.")
