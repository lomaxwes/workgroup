favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in favorite_languages.keys():  # можно указать favorite_languages без метода .keys()
    print(name.title())
print("-------------")
for value in favorite_languages.values():
    print(value.title())

