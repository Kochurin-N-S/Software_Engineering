def make_set(usr_list):
    result_list = list()
    for elem in usr_list:
        counter_of_elem = usr_list.count(elem)
        for replay in range(2, counter_of_elem + 1):
            line = str(elem) * replay
            result_list.append(line)
            usr_list.remove(elem)
        result_list.append(elem)
    return set(result_list)


list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(make_set(list_1))
print(make_set(list_2))
print(make_set(list_3))