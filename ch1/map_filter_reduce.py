from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# map: υπολογισμός τετραγώνου κάθε τιμής
squared = list(map(lambda x: x**2, nums))
print("Τετράγωνα:", squared)  # Τετράγωνα: [1, 4, 9, 16, 25, 36]

# filter: διατήρηση μόνο των περιττών τιμών
evens = list(filter(lambda x: x % 2 == 0, squared))
print("Άρτιοι αριθμοί:", evens)  # Άρτιοι αριθμοί: [4, 16, 36]

# reduce: άθροισμα τιμών
total = reduce(lambda x, y: x + y, evens)
print("Σύνολο:", total)  # Σύνολο: 56


print(
    "Σύνολο:",
    reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, 
                                      map(lambda x: x**2, nums))),
) # Σύνολο: 56
