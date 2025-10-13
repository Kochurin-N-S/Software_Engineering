def show_personal_info(name, age, company='unnamed'):
    print(f'Имя: {name} Возраст: {age} Компания: {company}')


tom = ('григорий', 22)
show_personal_info(*tom)

bob = ('георгий', 41, 'Yandex')
show_personal_info(*bob)