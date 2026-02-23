import my_mod

print(my_mod.PI)  # 3.14159
print(my_mod.square(5))  # 25
print(my_mod.hello("Μαρία"))  # Hello, Μαρία!

print(my_mod.__file__)  # εμφανίζει το path του my_mod.py
print(my_mod.__name__)  # εμφανίζει "my_mod"
print(__name__)  # εμφανίζει "__main__"
print(my_mod.__doc__)  # εμφανίζει "Ένα απλό module χρήστη"
