import math
def area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * (radius ** 2)
print(area(5))  # Output: 78.53981633974483

def circumference(radius):
    """Calculate the circumference of a circle given its radius."""
    return 2 * math.pi * radius
print(circumference(5))  # Output: 31.41592653589793