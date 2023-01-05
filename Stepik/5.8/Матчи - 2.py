n = int(input())
com = []
for i in range(n):
    home, guest = map(int, input().split())
    com.append([home, guest])

count = 0
for i in range(n-1):
    for j in range(i+1, n):
        if com[i][0] == com[j][1]:
            count += 1
        if com[i][1] == com[j][0]:
            count += 1
print(count)