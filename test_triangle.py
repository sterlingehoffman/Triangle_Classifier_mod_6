from triangle import classify_triangle, is_valid_triangle
import math

def test_is_side_positive():
    assert not is_valid_triangle(0,1,2), "Triangle with zero side length should be invalid"
    print("Test Passed")

# Copilot suggested body for test, rejected as it included more than just the one test.
def test_is_inequal_triangle():
    assert not is_valid_triangle(1, 1, 3), "Triangle with sides 1, 1, 3 should be invalid"
    print("Test Passed")
    else:
        print("Valid")

# Copilot suggested body for test, edited to allow for correct testing of the case.
def test_is_degenerate_triangle():
    assert not is_valid_triangle(1, 2, 3), "Triangle with sides 1, 2, 3 should be invalid"
    print("Test Passed")

# Copilot suggested body for test, accepted as it correctly tests for the case.
def test_is_equilateral_triangle():
    assert classify_triangle(2, 2, 2) == "Equilateral", "Triangle with sides 2, 2, 2 should be equilateral"
    print("Test Passed")

# Copilot suggested body for test, accepted as it correctly tests for the case.
def test_is_isosceles_triangle():
    assert classify_triangle(2, 2, 3) == "Isosceles", "Triangle with sides 2, 2, 3 should be isosceles"
    print("Test Passed")

# Copilot suggested body for test, accepted as it correctly tests for the case.
def test_is_scalene_triangle():
    assert classify_triangle(2, 3, 4) == "Scalene", "Triangle with sides 2, 3, 4 should be scalene"
    print("Test Passed")

# Copilot suggested body for test, accepted as it correctly tests for the case.
def test_is_right_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene", "Triangle with sides 3, 4, 5 should be right scalene"
    print("Test Passed")

# Copilot suggested body for test, accepted as it correctly tests for the case.
def test_is_right_with_non_integer_sides():
    assert classify_triangle(5, 5, 5*math.sqrt(2)) == "Right Isosceles", "Triangle with sides 5, 5, 5*sqrt(2) should be right isosceles"
    print("Test Passed")

# Copilot suggested body for test, edited to allow for assignment specified test case to be tested.