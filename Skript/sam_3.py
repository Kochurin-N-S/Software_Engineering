from math import sqrt


def get_area(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p) * (p - a) * (p - b) * (p - c)


one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

triangle_min_sides = get_area(min(one), min(two), min(three))
triangle_max_sides = get_area(max(one), max(two), max(three))

print(f'площадь треугольника с минимальными сторонами - {triangle_min_sides}')
print(f'с максимальными - {triangle_max_sides}')