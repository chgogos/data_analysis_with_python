import re

text = """
Η συνάντηση θα γίνει στις 5-9-2025 και 
η επόμενη στις 12.10.25. Μια άλλη 
επιλογή είναι οι συναντήσεις να γίνουν 
1/10/25 και 17/10/2025 αντίστοιχα.
"""

date_pattern = r"\b(\d{1,2})[./-](\d{1,2})[./-](\d{2}|\d{4})\b"
matches = re.findall(date_pattern, text)
matches = re.findall(date_pattern, text)

for day, month, year in matches:
    print(f"Ημέρα: {day}, Μήνας: {month}, Έτος: {year}")