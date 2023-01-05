def check_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    text = text.replace("\n", "")
    reverse_text = text[::-1]
    if text == reverse_text:
        
        print(f"Строка ({text}) является палиндромом!")
    else:

        print(f"Строка ({text}) не является палиндромом!")

check_palindrome("Кит на море не романтик")
check_palindrome("test")