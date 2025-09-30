global result


def get_area(side_a, side_b, type_of):
    global result
    if type_of == 1:
        result = side_a * side_b  # прямоугольник
    else:
        result = side_a * side_b / 2  # треугольник


def get_info():
    type = int(input("1->прямоугольник 2->треугольник :"))
    a = float(input('введите первую сторону: '))
    b = float(input('введите вторую сторону: '))
    get_area(a, b, type)


if __name__ == '__main__':
    get_info()
    print(result)