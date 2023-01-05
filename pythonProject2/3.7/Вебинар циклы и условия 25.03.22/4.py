# a = [1, 'Hello', 5, 6, ['my luste', 8]]
# it = iter(a)
# try:
#    while True:
#        print(next(it))
# except StopIteration:
#   pass


a = [1, 'Hello', 5, 6, ['my luste', 8]]
for i in a:
    if type(i) == list:
        for l in i:
            print(l)
    else:
        print(i)