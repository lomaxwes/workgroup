n = list(map(int, input()))
last = [0]*10
for i in n:
    last[i] += 1
for i in range(len(last)):
    if last[i] > 0:
        print(i, last[i])
