a = int(input())
while True:
    if (a % 2) == 0:
        a = a // 2
        print(a)
        if a == 1:
            print(a)
            print("You win")
            break
    else:
        a = (a * 3 + 1) // 2
        print(a)



