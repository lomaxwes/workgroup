# Напишите программу, которая на вход принимает текст
# и выводит количество уникальных символов.

text = input("Введите текст:")

unique = set(text)

print("Количество уникальных символов: ", len(unique))


