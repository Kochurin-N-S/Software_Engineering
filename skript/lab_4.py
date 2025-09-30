def main(*args):
    one = args[0]
    two = sum(args)
    three = len(args)
    print(f'one = {one}, two = {two}, three = {three}!')
    return one + two / three


print(main(1, 2, 3, 4, 5))A