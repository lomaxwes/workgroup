def gen(a = []):

    while True:
        for i in a:
            yield i

# n = gen([1, 2, 3])


for i in gen([1, 2, 3]):
    print(i)

    # Решение скилл фэктори
def repeat_list(list_):
   list_values = list_.copy()
   while True:
       value = list_values.pop(0)
       list_values.append(value)
       yield value

for i in repeat_list([1, 2, 3]):
   print(i)
