# Ορισμός συνάρτησης με 1 παράμετρο
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


c = 0.0  # Θερμοκρασία σε βαθμούς Κελσίου
# Κλήσεις συνάρτησης
temp1 = celsius_to_fahrenheit(c)  # Όρισμα: 0
temp2 = celsius_to_fahrenheit(100)  # Όρισμα: 100
print(f"0°C = {temp1}°F")  # 0°C = 32.0°F
print(f"100°C = {temp2}°F")  # 100°C = 212.0°F
