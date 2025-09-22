userIn = int(input("Введите свое число: "))
if userIn in range(11):
    if userIn <= 3: print('от 0 до 3 включительно')
    elif userIn < 6: print('от 3 до 6;')
    else: print('от 6 до 10 включительно.')
else: print("Число не подходит!")