person = {} # с помощью фигурных скобок можно создать словарь
# словарь заполняется по принципу — ключ:объект (через двоеточие)

person = {'name' : 'Ivan Petrov'}

# в него можно также добавлять новые объекты по ключу
person['age'] = 24
person['email'] = 'petro@gmail.com'
person['phone'] = '89000000546'
print(person)
# Попытка извлечения объекта по несуществующему ключу приведёт к ошибке:
# print(person['address'])
# KeyError: 'address'

# Можно отдельно получить список ключей:
print(person.keys())

# Или список значений:
print(person.values())
# dict_values(['Ivan Petrov', 25, 'ivan_petrov@example.com', '8(800)555-35-35'])
person.pop('age')
print(person.values())