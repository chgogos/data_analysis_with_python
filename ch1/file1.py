filename = "lorem_ipsum.txt"
vowels = "aeiouAEIOU"
count = 0

f = open(filename, "r")
for line in f.read():
    for char in line:
        if char in vowels:
            count += 1
f.close()

print(f"Πλήθος φωνηέντων: {count}")  # Πλήθος φωνηέντων: 167
