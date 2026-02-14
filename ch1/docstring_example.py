import math


def calculate_area(radius):
    """
    Υπολογισμός του εμβαδού ενός κύκλου δεδομένης της ακτίνας του.

    Parameters:
    radius (float): Η ακτίνα του κύκλου.

    Returns:
    float: Το εμβαδόν του κύκλου.
    """
    return math.pi * radius**2


print(calculate_area.__doc__)
