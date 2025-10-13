def remove_from_tuple(tpl, elem):
    if elem not in tpl:
        return tpl
    else:
        result = list(tpl)
        result.remove(elem)
        return tuple(result)


print(remove_from_tuple((1, 2, 3), 1))
print(remove_from_tuple((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 1))
print(remove_from_tuple((2, 4, 6, 6, 4, 2), 9))