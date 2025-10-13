from pprint import pprint

my_dict = {'first': 'so easy'}


def dict_maker(**kwargs):
    global my_dict
    my_dict.update(kwargs)


dict_maker(a1=1, a2=20, a3=52, a4=13)
dict_maker(name='qwe', age=31, weight=70, eyes_color='blue')
pprint(my_dict)