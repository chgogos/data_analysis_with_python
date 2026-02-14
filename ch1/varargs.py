def my_function(*args):
    print(f"Ελήφθησαν {len(args)} ορίσματα")
    for i, arg in enumerate(args):
        print(f"Όρισμα {i}: {arg}", end=" ")
    print("\n")


my_function()  # 0 ορίσματα
my_function(1)  # 1 όρισμα
my_function(1, 2, 3)  # 3 ορίσματα
my_function("a", "b", "c", "d")  # 4 ορίσματα
