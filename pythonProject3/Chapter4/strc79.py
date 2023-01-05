foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print("The irst three items in the list are:")
for food in foods[0:3]:
    print(food.title())
print("Three items from the middle of the list are:")
for food in foods[1:4]:
    print(food.title())
print("The last three items in the list are:")
for food in foods[:-4:-1]:          # последние три из списка в перевернутом виде
    print(food.title())

friend_pizzas = foods[:]
foods.append('carbonara')
friend_pizzas.append('italiano')
print("My favorite pizzas are:")
for food in foods:
    print(food.title())
print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
print(foods is friend_pizzas)