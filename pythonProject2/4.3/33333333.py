


    # def incorrect_func(name_arg=[]):
    #    # name_arg является локальной переменной
    #    print("Аргумент до изменения", name_arg)
    #    name_arg.append(1)
    #    print("Аргумент после изменения", name_arg)
    #
    # # вызовем два раза одну и ту же функцию
    # incorrect_func()
    # print('-----')
    # incorrect_func()
    # incorrect_func()
    # incorrect_func()

# def correct_func(name_arg=None):
#    if name_arg is None:
#        name_arg = []
#    print("Аргумент до изменения", name_arg)
#    name_arg.append(1)
#    print("Аргумент после изменения", name_arg)
#
# # вызовем два раза одну и ту же функцию
# correct_func()
# print('-----')
# correct_func()
# print('-----')
# correct_func([555])
# print('-----')
# correct_func(name_arg=[555])
# text = "12345"
# print(len(text))
# print(type(text))
# print(text[0])
# print(text.index('3'))
n = 265465
print(n % 10)
print(n // 10)