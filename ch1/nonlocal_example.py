def shopping_cart():
    total = 0  # εξωτερική μεταβλητή για την add_items()

    def add_items(prices):
        nonlocal total  # επιτρέπει τροποποίηση της total
        for price in prices:
            total += price
            print(f"+{price:>2}, νέο σύνολο {total:>2}")

    add_items([10, 25, 5])
    print(f"Τελικό σύνολο: {total}")


shopping_cart()
