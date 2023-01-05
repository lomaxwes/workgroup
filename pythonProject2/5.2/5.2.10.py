# Уникальные буквы

def unique_letters(text):
    text = text.lower()
    text = text.replace(" ", "")
    text = text.replace("\n", "")
    spisok = []
    count = 0
    for i in text:
        if i in spisok:
            pass
        else:
            spisok.append(i)
            count += 1

    print(f" Количество уникальные буквы: {count}")
    print(spisok)


unique_letters("The Zen of Python")