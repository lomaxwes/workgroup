numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numbers:
    if i == 1:
        print(f"{i}st", end=' ')
    elif i == 2:
        print(f"{i}nd", end=' ')
    elif i == 3:
        print(f"3rd", end=' ')
    else:
        print(f"{i}th", end=' ')