def calculate_interest(principal, rate=0.05, time=1, compound_frequency=1):
    amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    interest = amount - principal
    return round(interest, 2)


# default τιμές: επιτόκιο 5%, 1 έτος, ετήσια εφαρμογή επιτοκίου
interest1 = calculate_interest(1000)
print(f"Τόκοι: {interest1}€")  # Τόκοι: 50.0€

# Προσαρμοσμένες τιμές: επιτόκιο 8%, 2 έτη, ετήσια εφαρμογή επιτοκίου
interest2 = calculate_interest(1000, rate=0.08, time=2)
print(f"Τόκοι: {interest2}€")  # Τόκοι: 166.4€
