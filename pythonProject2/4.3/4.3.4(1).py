def revers(text):
    if len(text) == 0:
        return text
    return revers(text[1:]) + text[0]

print(revers("123"))