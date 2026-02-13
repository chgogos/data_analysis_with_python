# Συνάρτηση που δεν επιστρέφει τιμή
def print_greeting(name):
    print(f"Γεια σου {name}!")


# Συνάρτηση που επιστρέφει μια τιμή
def calculate_area(length, width):
    area = length * width
    return area


# Κλήση συνάρτησης που δεν επιστρέφει τιμή
print_greeting("Μαρία")  # Γεια σου Μαρία!

# Κλήση συνάρτησης που δεν επιστρέφει τιμή και ανάθεση σε μεταβλητή
result = print_greeting("Ελένη")  # Γεια σου Ελένη!
print("Αποτέλεσμα:", result)  # Αποτέλεσμα: None

# Κλήση συνάρτησης calculate_area()
area = calculate_area(4.5, 3.2)
print(f"Το εμβαδόν είναι: {area} τ.μ.")  # Το εμβαδόν είναι: 14.4 τ.μ.
