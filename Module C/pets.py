from cat import Cat

cat1 = Cat('Семён', 'мальчик', 2)
cat2 = Cat('Боря', 'мальчик', 1)
cat3 = Cat('Муся', 'девочка', 4)

print("cat1.Имя - ", cat1.get_name())
print("cat2.Имя - ", cat2.get_name())
print("cat3.Имя - ", cat3.get_name())

print("cat1.Пол - ", cat1.get_gender())
print("cat2.Пол - ", cat2.get_gender())
print("cat3.Пол - ", cat3.get_gender())

print("cat1.Возраст - ", cat1.get_age())
print("cat2.Возраст - ", cat2.get_age())
print("cat3.Возраст - ", cat3.get_age())