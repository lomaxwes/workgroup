
# Из заданного списка вывести только положительные элементы
def positive(x):
    return x > 0  # функция возвращает только True или False


result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))   # [1, 2]

# def map_(func, some_list):
#     # some_list объект, над которым будет производиться преобразование
#     # func функция, которая должна выполняться над каждым объектом
#     outp = []
#     for i in range(len(some_list)):
#         outp.append(func(some_list[i]))
#     return outp
#
#
# map(function, iter1, iter2, ...)
#
# a_list = [1, 4, 9]
#
# print(list(map(pow, a_list)))  # [1, 4, 9]

# for i in map(pow_, a_list):
#    pass