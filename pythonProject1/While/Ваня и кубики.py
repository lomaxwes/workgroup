# Ване на день рождения подарили n кубиков.
# Он с друзьями решил построить из них пирамиду.
# Ваня хочет построить пирамиду следующим образом:
# на верхушке пирамиды должен находиться 1 кубик,
# на втором уровне — 1+2=3 кубика, на третьем — 1+2+3=6 кубиков,
# и так далее. Таким образом, на i-м уровне пирамиды должно
# располагаться 1+2+...+(i-1)+i кубиков.
n = int(input())
count = 0
i = 0
while (i + count) < n:
    count += 1
    i += count
    n -= i
print(count)