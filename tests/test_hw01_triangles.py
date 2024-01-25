from src.hw01_triangles import classify_triangle

from hypothesis import given, strategies as st, assume


@given(
    a=st.integers(min_value=1), b=st.integers(min_value=1), c=st.integers(min_value=1)
)
def test_valid_triangles_ints(a: int, b: int, c: int):
    assume(a + b > c and a + c > b and b + c > a)
    assert classify_triangle(a, b, c) != "NotATriangle"


@given(
    a=st.floats(min_value=0.1, max_value=100000000),
    b=st.floats(min_value=0.1, max_value=100000000),
    c=st.floats(min_value=0.1, max_value=100000000),
)
def test_valid_triangles_floats(a: float, b: float, c: float):
    assume(a + b > c and a + c > b and b + c > a)
    assert classify_triangle(a, b, c) != "NotATriangle"


@given(
    a=st.integers(min_value=1), b=st.integers(min_value=1), c=st.integers(min_value=1)
)
def test_invalid_triangles(a: int, b: int, c: int):
    assume(not (a + b > c and a + c > b and b + c > a))
    assert classify_triangle(a, b, c) == "NotATriangle"


@given(num=st.integers(min_value=1))
def test_equilateral_triangle(num: int):
    assert classify_triangle(num, num, num) == "Equilateral"


def test_right_triangle_simple():
    assert "Right" in classify_triangle(3, 4, 5)
    assert "Right" in classify_triangle(1, 1, 2**0.5)
    assert "Right" in classify_triangle(2**0.5, 1, 1)


@given(a=st.integers(min_value=1), b=st.integers(min_value=1))
def test_isosceles_triangle(a: int, b: int):
    assume(a != b)
    assert "Isosceles" in classify_triangle(a, b, b)
    assert "Isosceles" in classify_triangle(b, a, b)
    assert "Isosceles" in classify_triangle(b, b, a)


@given(a=st.integers(min_value=1), b=st.integers(min_value=1))
def test_right_triangle(a: int, b: int):
    assert "Right" in classify_triangle(a, b, (a**2 + b**2) ** 0.5)
    assert "Right" in classify_triangle(b, a, (a**2 + b**2) ** 0.5)
    assert "Right" in classify_triangle(b, (a**2 + b**2) ** 0.5, a)
    assert "Right" in classify_triangle((a**2 + b**2) ** 0.5, b, a)
    assert "Right" in classify_triangle((a**2 + b**2) ** 0.5, a, b)
    assert "Right" in classify_triangle(a, (a**2 + b**2) ** 0.5, b)
