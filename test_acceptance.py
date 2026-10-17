from triangle import classify_triangle

def test_acceptance():
    # Invalid side lengths produce a user-facing message.
    assert classify_triangle(0, 4, 5) == "Not a triangle", "Triangle with sides 0, 4, 5 should be invalid"

    # Classification completes without an unhandled exception.
    for sides in [(3, 4, 5), (4, 5, 6), (1, 2, 3), (0, 4, 5)]:
        result = classify_triangle(*sides)
        assert result is not None
