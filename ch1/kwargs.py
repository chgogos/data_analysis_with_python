def my_function(**kwargs):
    print(f"Ελήφθησαν {len(kwargs)} ονοματισμένα ορίσματα")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


my_function()  # 0 ορίσματα
my_function(name="Νίκος")  # 1 ονοματισμένο όρισμα
my_function(name="Μαρία", age=30)  # 2 ονοματισμένα ορίσματα
my_function(city="Ιωάννινα", country="GR", population=115000)  # 3 ον. ορ.
