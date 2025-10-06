import random

a = [int(random.random() * 100) for i in range(20)]
print(f'исходный список - {a}')
a.sort()
print(f'отсортированный список - {a}')
a.pop(0)
print(f'новый список - {a}')