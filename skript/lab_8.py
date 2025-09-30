from math import sqrt, sin, cos


def main():
    value = int(input("enter your value -> "))
    print(f'корень : {sqrt(value)}\n'
          f'синус : {sin(value)}\n'
          f'косинус : {cos(value)}')


if __name__ == '__main__':
    main()