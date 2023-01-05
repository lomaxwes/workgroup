def ladder_stars(n):
    for i in reversed(range(1, n + 1)):
        n = i * "*"
        print(n)

ladder_stars(20)

