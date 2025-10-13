request = int(input('Введите номер кабинета: '))

cab_status = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1334, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': False},
    None: {'key': None, 'access': False},
}

response = cab_status.get(request, False)
if not response:
    response = cab_status[None]
key = response.get('key')
access = response.get('access')
print(key, access)