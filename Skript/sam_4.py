list1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
list2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
list3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]


def replace_assessments(a_list):
    new_list = list()
    for i in range(len(a_list)):
        if a_list[i] == 2:
            continue
        if a_list[i] == 3:
            new_list.append(4)
            continue
        new_list.append(a_list[i])

    return new_list


print(replace_assessments(list1))
print(replace_assessments(list2))
print(replace_assessments(list3))