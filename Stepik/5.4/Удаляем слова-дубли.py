s = list(input().split())
low = []
last = []
for i in range(len(s)):
    if s[i].lower() not in low:
        low.append(s[i].lower())
        last.append(s[i])
print(' '.join(last))