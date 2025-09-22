value = 50

while value > 0:
    if value % 2 == 0:
        print(value)
        if value % 10 == 0:
            print(f'######{value // 10}#######')
    if value < 0:
        break
    value -= 1