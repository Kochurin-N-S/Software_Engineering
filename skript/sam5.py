string = input("Введите текст для поиска: ")
with open('stat.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    text = text.lower()
    count = text.count(string.lower())
    print(f"'{string}' встречается в тексте {count} раз(а).")