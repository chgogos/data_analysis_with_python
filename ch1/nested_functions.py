def total_price(base_price, tax_rate):
    # εσωτερική συνάρτηση: υπολογίζει το φόρο
    def tax(amount):
        return amount * tax_rate

    # κλήση εσωτερικής συνάρτησης
    tax_amount = tax(base_price)
    return base_price + tax_amount


print(total_price(100, 0.24))  # 124.0
print(total_price(50, 0.10))  # 55.0
