from random import randint


def dice():
    cast = randint(1, 6)
    print(f'вам выпало {cast}!')
    if cast <= 2:
        print('вы проиграли!')
    elif cast <= 4:
        print('переброс...')
        dice()
    else:
        print('вы победили!')


if __name__ == '__main__':
    dice()