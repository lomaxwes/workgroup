# def palindrom(text):
#     text = text.lower()
#     text = text.replace(" ", "")
#     text = text.replace("\n","")
#     if text == text[::-1]:
#         print("Текст является палинромом!")
#     else:
#         print("Текст не является палинромом!")
#
# palindrom("Кит на море не романтик")
# palindrom("А роза упала на лапу Азора")

def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])

print(palindrom("шалаш"))