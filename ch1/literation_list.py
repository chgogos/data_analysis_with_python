numbers = [10, 20, 30]

i = 0
while i < len(numbers):
    print(numbers[i], end=" ")
    i += 1

print(); print("-" * 8)
for i in range(len(numbers)):
    print(numbers[i], end=" ")

print(); print("-" * 8)
for num in numbers:
    print(num, end=" ")

print(); print("-" * 8)
for index, num in enumerate(numbers):
    print(f"Θέση {index}: {num}", end=" ")