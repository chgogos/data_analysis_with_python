class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate


savings = SavingsAccount("Γιάννης Παπαδόπουλος", 3000, 0.05)
print(f"Αρχικό υπόλοιπο: {savings.balance:.2f} ευρώ")

for i in range(5):
    savings.apply_interest()
    print(f"Μετά από την {i+1}η εφαρμογή τόκων: {savings.balance:.2f} ευρώ")

print(f"Τελικό υπόλοιπο: {savings.balance:.2f} ευρώ")
