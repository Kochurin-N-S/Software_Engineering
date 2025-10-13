usr_list = input("enter your nums: ").split(' ')
data_list = [int(i) for i in usr_list]
data_tuple = tuple(data_list)
print('список -', data_list)
print('кортеж -', data_tuple)