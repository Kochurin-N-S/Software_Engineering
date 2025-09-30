from datetime import datetime  # импортировать функцию datetime из модуля datetime
from math import sqrt  # импортировать функцию sqrt из модуля math


# определение main() функции
def main(**kwargs):
    '''
    Вывод в консоль расстояния от начала координат до точки    :param kwargs: словарь    :return: None
    '''
    for key in kwargs.items():  # key = кортеж типа (ключ, значение)
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)  # вычисление расстояния
        print(result)  # вывод на экран


if __name__ == '__main__':  # точка входа в программу
    start_time = datetime.now()  # время с момента запуска программы
    # вызов main() и передача аргументов
    main(
    one = [10, 3],
    two = [5, 4],
    three = [15, 13],
    four = [93, 53],
    five = [133, 15]
)
time_costs = datetime.now() - start_time  # текущее время - время с момента запуска
print(f"Время выполнения программы - {time_costs}")  # вывод времени выполнения через f-строку