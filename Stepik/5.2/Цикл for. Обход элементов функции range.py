n = int(input())
list = []
for i in range(n):
    s = input()
    if 'соль' not in s:
        list.append(s)
print(', '.join(list))
