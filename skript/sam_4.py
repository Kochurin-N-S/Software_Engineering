def my_abs(*args):
    full_sum = 0
    for num in args:
        full_sum += num
    return full_sum / len(args)


if __name__ == '__main__':
    result = my_abs(123, 53, 6, 23, 5346, 7, 3, 1, -8, -99, )
    print(f'среднее арифметическое - {round(result, 2)}')