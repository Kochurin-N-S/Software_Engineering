from pprint import pprint


def who_is_faster(some_string):
    table = dict()
    help_set = set(tuple(some_string))

    for char in help_set:
        value = some_string.count(char)
        table.update({int(char): value})
    return table


result = who_is_faster(input("type here: "))
pprint(result)