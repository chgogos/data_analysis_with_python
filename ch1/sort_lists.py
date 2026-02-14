numbers = [3, 1, 4, 2]
numbers.sort()  # ταξινομεί την ίδια τη λίστα
print(numbers)  # [1, 2, 3, 4]

numbers = [3, 1, 4, 2]
print(sorted(numbers))  # [1, 2, 3, 4]
print(numbers)  # [3, 1, 4, 2]

words = ["μπανάνα", "ακτινίδιο", "μήλο"]
print(sorted(words, key=len))  # ['μήλο', 'μπανάνα', 'ακτινίδιο']
print(sorted(words, key=len, reverse=True))  # ['ακτινίδιο', 'μπανάνα', 'μήλο']
