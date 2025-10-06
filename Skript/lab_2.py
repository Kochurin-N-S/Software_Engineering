def add_elms(usr_list):
    for i in range(5):
        usr_list.add(i)
    print(usr_list)


my_set = {1, 2, 3, 4, 5}
my_frozen = frozenset(my_set)

add_elms(my_set)
print('*' * 20)
add_elms(my_frozen)