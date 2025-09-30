from sam_5g import triangle_area

side_a = float(input('Введите первую сторону --> '))
side_b = float(input('Введите вторую сторону --> '))

print(f'Площадь треугольника со сторонами {side_a} и {side_b} равна {triangle_area(side_a, side_b)}')