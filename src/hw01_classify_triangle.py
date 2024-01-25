import math

def classify_triangle(a,b,c):
    if a + b <= c or b + c <= a or a + c <= b:
        return "Invalid Triangle"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        if round(a*a) + round(b*b) == round(c*c):
            return "Right Isosceles Triangle"
        else:
            return "Isosceles Triangle"
    else:
        if round(a*a) + round(b*b) == round(c*c):
            return "Right Scalene Triangle"
        else:
            return "Scalene"

# Invalid Input
result = classify_triangle(0, 4, 5)
print(result)    

# Invalid Input
result = classify_triangle(1, 2, 3)
print(result)  

# Equilateral
result = classify_triangle(5, 5, 5)
print(result)

# Right Isosceles Triangle
result = classify_triangle(1, 1, math.sqrt(2))
print(result)

# Isosceles Triangle
result = classify_triangle(3, 5, 5)
print(result)

# Right Scalene Triangle
result = classify_triangle(3, 4, 5)
print(result)

# Scalene
result = classify_triangle(7, 10, 12)
print(result)