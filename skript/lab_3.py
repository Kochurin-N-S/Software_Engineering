def lab3(num_1, num_2):
    return num_1 * num_2


if __name__ == '__main__':
    result = 0
    for i in range(3):
        result += lab3(i + 1, 4)
    print(result)