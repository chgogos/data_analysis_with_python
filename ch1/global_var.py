# καθολική μεταβλητή
exchange_rate = 1.15  # EUR -> USD


def convert_to_usd(amount_eur):
    return amount_eur * exchange_rate


def update_rate(new_rate):
    global exchange_rate  # πρέπει να υπάρχει
    exchange_rate = new_rate


print(f"{convert_to_usd(50):.2f}") # 57.50
update_rate(1.2)
print(f"{convert_to_usd(50):.2f}") # 60.00
