x = int(input())
print(((x % 4 == 0) and not (x % 100 == 0) or (x % 400 == 0)))

# ((x % 400) ==0) and (x % 100) ==0) and
# or ((x % 4) == 0)