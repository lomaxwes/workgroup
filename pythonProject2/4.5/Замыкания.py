def main(value):
    name = value
    def inner():
        print('Hello asshole', name)
    return inner

s = main('Ivan')
r = main('Misha')
s()
r()

print(type(s))
