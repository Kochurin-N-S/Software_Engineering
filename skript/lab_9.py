from datetime import datetime as dt, timedelta as td

def main():
    today = dt.today()

    print(f'сегодня {today.date()}')
    print(f'день недели - {today.isoweekday()}')
    n = int(input("введите количество дней: "))
    result = today + td(days=n)
    print(f'через {n} дней будет {result.date()}')
    print(f'день недели - {result.isoweekday()}')

if __name__ == '__main__':
    main()