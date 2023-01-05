x = int(input())
y = int(input())
count = 1
while x <= y:
    count += 1
    x = x*1.1
    print(x)
print(count)