import math
from typing import Literal


def classify_triangle(a: float, b: float, c: float) -> str:
    tri_type: str = triangle_class(a, b, c)
    if tri_type == "NotATriangle":
        return tri_type

    if is_right_triangle(a, b, c):
        tri_type += " Right"
    return tri_type.strip()


def is_triangle(a: float, b: float, c: float) -> bool:
    """Returns True if a, b, and c can form a triangle, False otherwise."""
    return a + b > c and a + c > b and b + c > a


def triangle_class(
    a: float, b: float, c: float
) -> Literal["Equilateral", "Isosceles", "Scalene", "NotATriangle"]:
    """Returns the type of triangle, or "NotATriangle" if a, b, and c cannot form a triangle."""
    if not is_triangle(a, b, c):
        return "NotATriangle"
    if a == b == c:
        return "Equilateral"
    elif len(set([a, b, c])) == 2:
        return "Isosceles"
    else:
        return "Scalene"


def is_right_triangle(a: float, b: float, c: float) -> bool:
    """Returns True if a, b, and c form a right triangle, False otherwise."""
    return (
        math.isclose(a**2 + b**2, c**2, rel_tol=1e-3)
        or math.isclose(b**2 + c**2, a**2, rel_tol=1e-3)
        or math.isclose(a**2 + c**2, b**2, rel_tol=1e-3)
    )
