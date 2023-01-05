s = input()
if len(s) % 2 != 0:
    print("NO")
else:
    for i in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    if s == '':
        print("YES")
    else:
        print("NO")




