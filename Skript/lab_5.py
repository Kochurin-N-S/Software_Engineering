import random


def useless(usr_list):
    return max(usr_list) / len(usr_list)


print(useless([3, 4, 5, 6, 7, 33]))
print(useless([56, 1, 64, 1, 5, 1]))
print(useless([int(random.random() * 100) for i in range(5)]))