import math 
def is_valid_triangle(a, b, c):
    """
    Check if the given sides can form a valid triangle.

    A triangle is valid if the sum of any two sides is greater than the third side.

    Parameters:
    a (float): Length of side a
    b (float): Length of side b
    c (float): Length of side c

    Returns:
    bool: True if the sides can form a valid triangle, False otherwise.
    """
    return (a + b > c) and (a + c > b) and (b + c > a)
    # Used Copilot to generate this function, accepted as valid due to no flaws in the logic presented.

def classify_triangle(a, b, c):
    """
    Classify the type of triangle based on the lengths of its sides.

    Parameters:
    a (float): Length of side a
    b (float): Length of side b
    c (float): Length of side c

    Returns:
    str: Type of triangle or 'Not a triangle' if invalid, and prefixes with 'Right' if it is a right triangle.
    """
    if not is_valid_triangle(a, b, c):
        return "Not a triangle"
    str result = ""

    if a == b == c:
        result = "Equilateral"
    elif a == b or b == c or a == c:
        result = "Isosceles"
    else:
        result = "Scalene"

    # Check for right triangle using Pythagorean theorem
    sides = sorted([a, b, c,])
    if math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2):
        result = "Right " + result

    return result
    # Used Copilot to generate this function, edited as it did not include check to see if triangle was a right triangle.