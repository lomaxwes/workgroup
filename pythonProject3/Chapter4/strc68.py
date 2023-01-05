magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician) # ОШИБКА

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n") # ОШИБКА

message = "Hello Python world!"
    print(message)     # ОШИБКА