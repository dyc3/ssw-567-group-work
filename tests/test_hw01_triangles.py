from src.hw01_classify_triangle import classify_triangle, is_triangle, is_right_triangle

from hypothesis import given, strategies as st, assume


@given(
    a=st.integers(min_value=1), b=st.integers(min_value=1), c=st.integers(min_value=1)
)
def test_valid_triangles_ints(a: int, b: int, c: int):
    assume(is_triangle(a, b, c))
    assert classify_triangle(a, b, c) != "NotATriangle"


@given(
    a=st.floats(min_value=0.1, max_value=100000000),
    b=st.floats(min_value=0.1, max_value=100000000),
    c=st.floats(min_value=0.1, max_value=100000000),
)
def test_valid_triangles_floats(a: float, b: float, c: float):
    assume(is_triangle(a, b, c))
    assert classify_triangle(a, b, c) != "NotATriangle"


@given(
    a=st.integers(min_value=1), b=st.integers(min_value=1), c=st.integers(min_value=1)
)
def test_invalid_triangles(a: int, b: int, c: int):
    assume(not is_triangle(a, b, c))
    assert classify_triangle(a, b, c) == "NotATriangle"


@given(num=st.integers(min_value=1))
def test_equilateral_triangle(num: int):
    assert classify_triangle(num, num, num) == "Equilateral"


def test_right_triangle_simple():
    assert is_right_triangle(3, 4, 5)
    assert is_right_triangle(1, 1, 2**0.5)
    assert is_right_triangle(2**0.5, 1, 1)


@given(a=st.integers(min_value=1), b=st.integers(min_value=1))
def test_isosceles_triangle(a: int, b: int):
    assume(a != b)
    assume(a + b > b and b + b > a)
    assert "Isosceles" in classify_triangle(a, b, b)
    assert "Isosceles" in classify_triangle(b, a, b)
    assert "Isosceles" in classify_triangle(b, b, a)


@given(a=st.integers(min_value=1), b=st.integers(min_value=1))
def test_right_triangle(a: int, b: int):
    c = (a**2 + b**2) ** 0.5
    assume(is_triangle(a, b, c))
    assert is_right_triangle(a, b, c)
    assert is_right_triangle(b, a, c)
    assert is_right_triangle(b, c, a)
    assert is_right_triangle(c, b, a)
    assert is_right_triangle(c, a, b)
    assert is_right_triangle(a, c, b)


@given(
    a=st.floats(min_value=0.1, max_value=100000000),
    b=st.floats(min_value=0.1, max_value=100000000),
    c=st.floats(min_value=0.1, max_value=100000000),
)
def test_classify_output_format(a: float, b: float, c: float):
    assert classify_triangle(a, b, c) in (
        "Equilateral",
        "Isosceles",
        "Scalene",
        "Equilateral Right",
        "Isosceles Right",
        "Scalene Right",
        "NotATriangle",
    )
