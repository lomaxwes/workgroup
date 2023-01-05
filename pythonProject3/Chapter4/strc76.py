# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]   # копируте (создаёт) новый список с такими же елементами
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print(friend_foods == my_foods)
print(friend_foods is my_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)
