def calculate_rectangle_area(length, width):
    return length * width


r1 = calculate_rectangle_area(10, 20)  # ορίσματα θέσης
r2 = calculate_rectangle_area(length=10, width=20)  # ονοματισμένα ορίσματα
r3 = calculate_rectangle_area(width=20, length=10)  # ονοματισμένα ορίσματα
r4 = calculate_rectangle_area(
    10, width=10
)  # συνδυασμός ορισμάτων θέσης και ονοματισμένων ορισμάτων
print(f"{r1=}, {r2=}, {r3=}, {r4=}")  # r1=200, r2=200, r3=200, r4=100
