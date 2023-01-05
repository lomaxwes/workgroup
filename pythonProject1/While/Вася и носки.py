# У Васи есть n пар носков. Утром каждого дня,
# собираясь в школу, Вася должен надеть пару носков.
# Вечером, прийдя со школы, Вася снимает надетые носки
# и выбрасывает их. Каждый m-й день (в дни с номерами
# m,2m,3m,...) мама покупает Васе одну пару носков.
# Она делает это поздно вечером, поэтому Вася может
# надеть новые носки не раньше следующего дня.
# На сколько подряд идущих дней Васе хватит носков?

n, m = map(int, input().split())
day = 0
while n > 0:
    day += 1
    n -= 1
    if day % m == 0:
        n += 1
print(day)