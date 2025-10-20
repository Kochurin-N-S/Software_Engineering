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
<img width="532" height="453" alt="image" src="https://github.com/user-attachments/assets/ef040226-7c2c-4211-8175-6aabe3d46771" />

### Выводы
Создан текстовый файл для последующих операций чтения/записи.

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```

### Результат.

<img width="535" height="455" alt="image" src="https://github.com/user-attachments/assets/f005d218-5322-4d45-a33f-976122e7db6c" />

### Выводы
Освоено чтение первой строки файла с использованием конструкции open()/close().
## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```

### Результат.

<img width="765" height="439" alt="image" src="https://github.com/user-attachments/assets/9aa2a179-f06c-4721-8d7a-7d595cd792aa" />

### Выводы
Реализовано чтение всех строк файла в массив с помощью open()/close().
## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    print(f.readlines())
```

### Результат.

<img width="1024" height="525" alt="image" src="https://github.com/user-attachments/assets/b521ec8b-1c62-4135-ab51-9cf7a58bd910" />

### Выводы
Продемонстрировано чтение файла в массив с использованием менеджера контекста (with open()), обеспечивающего автоматическое закрытие файла.
## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```

### Результат.

<img width="1022" height="523" alt="image" src="https://github.com/user-attachments/assets/37d1cd5e-25dc-4cb7-83d7-1f6ed8a5ae5f" />

### Выводы
Освоено построчное чтение и вывод содержимого файла с помощью with open().
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

<img width="1025" height="522" alt="image" src="https://github.com/user-attachments/assets/4e359098-25fc-4781-9fcb-92b3aa344493" />

### Выводы
Реализовано добавление новой строки в файл в режиме 'a+' с последующей проверкой изменений.
## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```

### Результат.

<img width="1362" height="632" alt="image" src="https://github.com/user-attachments/assets/a879419c-c6b0-4a1c-a129-3ec2481f17dd" />

### Выводы
Освоено полное перезаписывание содержимого файла новыми данными в режиме 'w'.
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
print_docs('C:/Users/NickYcH/Desktop')
```

### Результат.

<img width="1284" height="651" alt="image" src="https://github.com/user-attachments/assets/d576c718-2a9e-4927-9a99-ae08bc05af90" />

### Выводы
Получены практические навыки рекурсивного обхода директорий и вывода их содержимого с помощью os.walk()
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

<img width="1066" height="661" alt="image" src="https://github.com/user-attachments/assets/10d25139-460a-4604-aa80-a2796602de27" />

### Выводы
Создана функция для поиска слова максимальной длины в текстовом файле.
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

<img width="1361" height="704" alt="image" src="https://github.com/user-attachments/assets/b8a4f055-bfcd-4542-9770-4d43fc0e7db9" />

### Выводы
Освоено создание CSV-файла с записью структурированных данных и использованием временных задержек.
## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация

###Скриншот файла со статьей:

<img width="1903" height="1067" alt="image" src="https://github.com/user-attachments/assets/d2a779d0-bdee-4764-9098-1b665c62e773" />

###Листинг кода:
```python
with open('stat.txt', 'r', encoding='utf-8') as f:
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

<img width="1364" height="705" alt="image" src="https://github.com/user-attachments/assets/abac4c0a-11c4-4b9d-8a6a-de03496d7b84" />

### Выводы
Разработан алгоритм подсчета общего количества слов и определения наиболее частотного слова в тексте
  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

###Скриншот файла с учетом расходов:

<img width="872" height="582" alt="image" src="https://github.com/user-attachments/assets/faef7156-ef87-4849-9c4b-53e54c713677" />

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
<img width="1420" height="1434" alt="image" src="https://github.com/user-attachments/assets/dbad17d5-08ef-43e7-bd11-8ef12933e2ee" />

### Выводы
Создана система учета расходов с интерактивным консольным интерфейсом для ввода и просмотра данных.
  
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

<img width="1207" height="685" alt="image" src="https://github.com/user-attachments/assets/e6399994-69e9-4a66-953a-27ce82161e04" />

### Выводы
Реализован анализ текстового файла с подсчетом букв, слов и строк.

  
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

<img width="1207" height="691" alt="image" src="https://github.com/user-attachments/assets/1eb7ef7d-6327-4ef8-b937-b129eed837a9" />

### Выводы
Освоена цензура текста путем замены запрещенных слов с использованием регулярных выражений.
  
## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

###Задание:
###Напишите программу, которая находит часть текста в текстовом файле и считает ее количество.

```python
string = input("Введите текст для поиска: ")
with open('stat.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    text = text.lower()
    count = text.count(string.lower())
    print(f"'{string}' встречается в тексте {count} раз(а).")
```

### Результат.

<img width="1123" height="662" alt="image" src="https://github.com/user-attachments/assets/8c088eb6-12ef-45e0-b0ce-6374168d414f" />

### Выводы
Разработана программа для поиска и подсчета вхождений заданной подстроки в текстовом файле.
## Общие выводы по теме

В ходе изучения темы освоены ключевые операции работы с файлами в Python: создание, чтение, запись, добавление данных. Приобретены навыки использования различных режимов открытия файлов, работы с текстовыми и CSV-форматами, а также реализации практических задач по обработке и анализу файловых данных.
