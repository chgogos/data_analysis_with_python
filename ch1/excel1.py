from openpyxl import load_workbook

# 1. Φόρτωση αρχείου Excel (Workbook)
wb = load_workbook("orders.xlsx")
# 2. Πρόσβαση σε φύλλο (Sheet)
sheet = wb["Orders"]
# 3a. Ανάγνωση κελιών
print("Πρώτη σειρά του φύλλου:")
for cell in sheet[1]:  # 1η γραμμή (header)
    print(cell.value, end="\t")
print("\n")
# 3b. Ανάγνωση συγκεκριμένων κελιών
order_id = sheet["A2"].value
product = sheet["B2"].value
quantity = sheet["C2"].value
print(f"Order ID: {order_id}, Product: {product}, Quantity: {quantity}")
# 3c. Εγγραφή σε κελιά
sheet["A4"] = 102  # Αριθμός παραγγελίας
sheet["B4"] = "ΖΑΧΑΡΗ 1 ΚΙΛΟ"  # Προϊόν
sheet["C4"] = 1  # Ποσότητα
# 3d. Ενημέρωση κελιού
sheet["C2"] = quantity + 2  # αύξηση ποσότητας παραγγελίας
# 4. Αποθήκευση αλλαγών
wb.save("orders_updated.xlsx")
print("Οι αλλαγές αποθηκεύτηκαν στο 'orders_updated.xlsx'.")
