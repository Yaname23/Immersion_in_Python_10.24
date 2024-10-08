# задача с треугольником
def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник с такими сторонами не может существовать"
    if a != b and b != c and a != c:
        return "Этот треугольник разносторонний"
    elif a == b and b == c:
        return "Этот треугольник равносторонний"
    else:
        return "Треугольник равнобедренный"

print(triangle_type(6, 7, 8))
print(triangle_type(5, 5, 5))
print(triangle_type(4, 4, 3))

