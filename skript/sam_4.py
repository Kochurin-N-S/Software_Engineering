def line_info(line):
    chars = ['a', 'e', 'i', 'o', 'u']

    print(f'Исходная строка - {line}')
    print(f'Длина предложения: {len(line)}')
    line = str.lower(line)
    print(line)

    counter = 0
    for char in line:
        if char in chars: counter += 1
    print(f'Количество гласных: {counter}')

    line = str.replace(line, 'ugly', 'beautiful')
    print(line)

    if line[:3] == 'the' or line[-3:] == 'end':
        print('Предложение начинается с "The" или заканчивается на "end".')
    print("####################################################")


line_info("SoMe LinE")
line_info("The ugly world")
line_info("aeiou end")