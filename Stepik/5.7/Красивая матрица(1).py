n = 5
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            point1, point2 = i, j
moves = abs(point1 - 2) + abs(point2 - 2)
print(moves)