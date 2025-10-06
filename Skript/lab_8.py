from random import randint


def list_maker():
    return [randint(1, 100)] * randint(3, 10)


if __name__ == '__main__':
    result = []
    for i in range(randint(1, 5)):
        result.append(list_maker())
    print(result)
