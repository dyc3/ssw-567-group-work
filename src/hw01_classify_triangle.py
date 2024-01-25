"Module to creat classify_traingle function."


def classify_triangle(a, b, c):
    "Function classifying traingle into different types based on each side's length."
    if a + b <= c or b + c <= a or a + c <= b:
        return "Invalid Triangle"
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        if round(a * a) + round(b * b) == round(c * c):
            return "Right Isosceles Triangle"
        return "Isosceles Triangle"
    if round(a * a) + round(b * b) == round(c * c):
        return "Right Scalene Triangle"
    return "Scalene"
