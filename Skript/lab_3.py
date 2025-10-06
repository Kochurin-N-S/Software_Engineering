def replace(usr_list):
    usr_list[0], usr_list[-1] = usr_list[-1], usr_list[0]
    return usr_list


my_list = [1, 2, 3]
print(replace(my_list))