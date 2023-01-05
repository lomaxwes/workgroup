f = open('C:/Users/And/Desktop/wot/input.txt', 'r', encoding='utf8')
for line in f:
    if int(line.split()[-1]) < 3:
        " ".join(line.split()[:-1])


with open('C:/Users/And/Desktop/wot/input.txt', encoding="utf8") as file:
    for line in file:
        points = int(line.split()[-1])
        if points < 3:
            name = " ".join(line.split()[:-1])
            print(name)