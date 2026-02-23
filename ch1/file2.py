filename = "lorem_ipsum.txt"
vowels = "aeiouAEIOU"
count = 0

with open(filename, "r") as f:
    for line in f.read():
        for char in line:
            if char in vowels:
                count += 1

print(f"Πλήθος φωνηέντων: {count}")  # Πλήθος φωνηέντων: 167
