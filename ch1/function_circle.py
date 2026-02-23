import math


def circle_properties(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    return diameter, circumference, area


diam, circum, area = circle_properties(5)
print(f"Διάμετρος: {diam:.2f}")  # Διάμετρος: 10.00
print(f"Περίμετρος: {circum:.2f}")  # Περίμετρος: 31.42
print(f"Εμβαδόν: {area:.2f}")  # Εμβαδόν: 78.54
