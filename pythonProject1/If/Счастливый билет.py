
num = int(input())
if (num // 100000 % 10 + num // 10000 % 10 + num // 1000 % 10) == (num // 100 % 10 + num // 10 % 10 + num % 10):
    print("YES")
else:
    print("NO")