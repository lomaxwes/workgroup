def rec(text):
    if len(text) == 1:
        return text
    else:
        return rec(text[1:]) + "*" + text[0]

print(rec("dfgdfhfghfghfgh"))