a = [23, 11, 33, 44, 22, 18, 32, 4, 7, 29, 4]
chet = []
nechet = []
for i in a:
    if i % 2 == 0:
        chet.append(i)
    else:
        nechet.append(i)
print(chet)
print(nechet)