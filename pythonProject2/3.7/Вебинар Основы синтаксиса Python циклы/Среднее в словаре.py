people = { 1: { 'name': 'Oleg', 'age': '29', 'sex': 'Male'},
           2: { 'name': 'Kate', 'age': '21', 'sex': 'Female'},
           3: { 'name': 'Liza', 'age': '24', 'sex': 'Female'},
           4: { 'name': 'Pavel', 'age': '36', 'sex': 'Male'}
}

print(people.items())
print(people.values())

age = 0
name = ''
for first in people.values():
    age += int(first['age'])
    name += first['name']
    print(first)
print(age/len(people))
