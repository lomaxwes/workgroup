d = {
    "Ivan": 1,
    "Max": 2,
    "Slon": 10,
}
print(sum(d.values()))

name = input()
print(d[name])

name = input()
amount = int(input())
d[name] += amount
print(d)