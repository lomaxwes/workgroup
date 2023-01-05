# while True:
#     name = input("Введите имя: ")
#     print(name)
#     add = input("Добавить учителя: ")
#     if add == 'no':
#         break
teachers = []
while True:

        full_name = input("Введите фио учителя: ")
        years = input("Сколько лет работает?: ")
        classes = input("Сколько предметов ведет?: ")
        salary = input("Какая зарплата?: ")
        add = input("Добавим еще учителя?: ")
        teachers.append(full_name)
        teachers.append(years)
        teachers.append(classes)
        teachers.append(salary)

        print()
        print("Учитель: ", full_name)
        print("Отработано лет: ", years)
        print("Предметов ведет: ", classes)
        print("Зарплата: ", salary)
        print()

        add = add.lower()
        if add == "да":
                continue
        if add == "нет":
                break
        else:
                print("Упс.. что то не то тыкнул ты мудак")
print(teachers)