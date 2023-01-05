favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("")
friends = ['phil', 'sarah', 'erin']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print("")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    if 'erin' in friends:
        friend = friends[2].title()
        print(f"Hello my friend {friend}!")
print("")
print(favorite_languages['sarah'])
