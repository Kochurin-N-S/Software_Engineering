# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
- Кочурин Никита Сергеевич
- ИВТ-23-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк

### Результат.

### Выводы

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```

### Результат.

### Выводы

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```

### Результат.

### Выводы

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    print(f.readlines())
```

### Результат.

### Выводы

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```

### Результат.

### Выводы

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```

### Результат.

### Выводы

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

lab47.py:
```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```

### Результат.

### Выводы

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os


def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)


print_docs('/Users/Andrey/Downloads')
```

### Результат.

### Выводы

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст: 
Приветствие 
Спасибо 
Извините 
Пожалуйста 
До свидания 
Ты готов? 
Как дела? 
С днем рождения! 
Удача! 
Я тебя люблю. 
Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных.

```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words


print(longest_words('input.txt'))
```

### Результат.

### Выводы

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами: 
• № - номер по порядку (от 1 до 300);
• Секунда – текущая секунда на вашем ПК;
• Микросекунда – текущая миллисекунда на часах. 
Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```

### Результат.

### Выводы

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация

###Скриншот файла со статьей:

###Листинг кода:
```python
with open('sam71input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    word_count = {}
    for line in lines:
        words = line.split()
        for word in words:
            word = word.strip('.,!?"«»:;–-—()%')
            if not word.isdigit():
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    sorted_count = dict(sorted(word_count.items(), key=lambda item: item[1]))
    most_used_word = sorted_count.popitem()
    print(f"Количество слов в тексте: {sum(word_count.values())}")
    print(f"Самое встречаемое слово: '{most_used_word[0]}', встречается {most_used_word[1]} раз.")
```

### Результат.

## Выводы

  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

###Скриншот файла с учетом расходов:

###Листинг кода:
```python
def input_expenses():
    name = input("\nВведите название расходов: ")
    amount = float(input("Введите сумму расходов: "))

    with open('expenses.txt', 'a', encoding='utf-8') as f:
        f.write(f"{name}: {amount} руб.\n")


def display_expenses():
    try:
        with open('expenses.txt', 'r', encoding='utf-8') as f:
            expenses = f.read()
            print("\nСуществующие расходы:")
            print(expenses)
    except FileNotFoundError:
        print("\nФайл не найден.")


def main():
    while True:
        print("\n1. Ввести информацию о расходах")
        print("2. Вывести существующие расходы")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            input_expenses()
        elif choice == "2":
            display_expenses()
        elif choice == "3":
            break
        else:
            print("\nВведите от 1 до 3!")


if __name__ == "__main__":
    main()
```

### Результат.

## Выводы

  
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк. 
• Текст в файле: 
Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 
• Ожидаемый результат: 
Input file contains: 108 
letters 20 words 
4 lines

```python
with open('input.txt', 'r') as f:
    lines = f.readlines()
    count_letters = 0
    count_words = 0
    count_lines = 0
    for line in lines:
        count_lines += 1
        words = line.split()
        count_words += len(words)
        for char in line:
            if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
                count_letters += 1
    print(count_letters, "letters")
    print(count_words, "words")
    print(count_lines, "lines")
```

### Результат.

## Выводы

  
## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****. 
• Запрещенные слова: 
hello email python the exam wor is 
• Предложение для проверки: 
Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!! 
• Ожидаемый результат: 
*****, ***ld! ****** ** *** programming language of *** future. My ***** **.... ****** ** awesome!!!!

```python
import re

sentence = 'Hello, world! Python IS the programming language of thE future. My EMAIL is.... \nPYTHON is awesome!!!!'
with open('input.txt', 'r') as f:
    ban_words = f.readline().split()
    for word in ban_words:
        sentence = re.sub(word, len(word)*'*', sentence, flags=re.IGNORECASE)
print(sentence)
```

### Результат.

## Выводы

  
## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

###Задание:
###Напишите программу, которая находит часть текста в текстовом файле и считает ее количество.

```python
string = input("Введите текст для поиска: ")
with open('sam71input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    text = text.lower()
    count = text.count(string.lower())
    print(f"'{string}' встречается в тексте {count} раз(а).")
```

### Результат.

## Выводы

## Общие выводы по теме

В результате ознакомления с теоретическим материалом и выполнения лабораторных и самостоятельных работ, я научился работать с файлами в Python.
