# С помощью генератора инициализируем двухмерный список

n = 3
m = 6

a = [[0]*m for i in range(n)]
a[1][3] = 50  # присваимаем 50 третьему значению во втором списке (т.к. 0 это первый список)

for i in a:      # разбиваем вложенные списки по строкам
    print(i)

print()

b = [[1]*m for i in range(n)]    # всем элементам списка (в том числе и вложенным)
# присваиваем 1.
for i in b:      # разбиваем вложенные списки по строкам
    print(i)
