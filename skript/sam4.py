tuple_1 = (1, 2, 3)
tuple_2 = (1, 8, 3, 4, 8, 8, 9, 2)
tuple_3 = (1, 2, 8, 5, 1, 2, 9)


def my_func(tpl, key):
    if key not in tpl:
        result = tuple()
        return result
    elif tpl.count(key) == 1:
        return tpl[tpl.index(key):]
    else:
        fi = tpl.index(key)
        si = tpl.index(key, fi + 1)
        return tpl[fi: si + 1]


print(my_func(tuple_1, 8))
print(my_func(tuple_2, 8))
print(my_func(tuple_3, 8))