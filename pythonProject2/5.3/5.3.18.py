text = 'aaabbccccdaa'

last = text[0]
result = ''
count = 0
for i in text:
    if i == last:
        count += 1
    else:
        result += last + str(count)
        last = i
        count = 1
result += last + str(count)
print(result)












