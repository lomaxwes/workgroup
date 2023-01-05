
field = [ 1, 2, 3,
          4, 5, 6,
          7, 8, 9
          ]


victory = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]
           ]

moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print()

def data_field():
    print("Поле боя крестиков и ноликов!\n")
    print(f"\t-------------")
    print(f"\t| {field[0]}\t| {field[1]}\t| {field[2]} |")
    print(f"\t-------------")
    print(f"\t| {field[3]}\t| {field[4]}\t| {field[5]} |")
    print(f"\t-------------")
    print(f"\t| {field[6]}\t| {field[7]}\t| {field[8]} |")
    print(f"\t-------------")
    print()

def vict():  # сравнение с полем возможных побед
    win = ''
    for elem in victory:
        if field[elem[0]] == "X" and field[elem[1]] == "X" and field[elem[2]] == "X":
            win = "Победил игрок X"
        if field[elem[0]] == "0" and field[elem[1]] == "0" and field[elem[2]] == "0":
            win = 'Победил игрок 0'

    return win

while True:

    data_field()

    str_moves = [str(i) for i in moves]
    display_row = ', '.join(str_moves)

    try:
        motion = int(input(f"Ваш ход - крестики. Выберите поле с номером - {display_row} : "))
    except ValueError:
        print()
        print("Необходимо выбирать номер поля. Попробуйте ещё раз!")
        break
    print()

    if motion in moves:
        moves.remove(motion)    # чтобы ход не дублировался
        motion -= 1             # уменьшаем, т.к. в списке элементы начинаются с 0
        field[motion] = 'X'     # записываем икс в поле выбранное игроком
    else:
        print("Так нельзя, конец игре!")
        break

    win = vict()
    if win != '':
        data_field()
        print(f"Поздравляем с победой! {win}")
        break

    if len(moves) == 0:
        print("Игра закончилась ничьей!")
        break

    data_field()                # выводим игровое поле

    str_moves = [str(i) for i in moves]
    display_row = ', '.join(str_moves)

    try:
        motion = int(input(f"Ход - нолики. Введите любое число из предложенных - {display_row}: "))
    except ValueError:
        print()
        print("Необходимо выбирать номер поля. Попробуйте ещё раз!")
        break
    print()

    if motion in moves:
        moves.remove(motion)    # чтобы ход не дублировался
        motion -= 1             # уменьшаем, т.к. в списке элементы начинаются с 0
        field[motion] = '0'     # записываем ноль в поле выбранное игроком
    else:
        print("Так нельзя, конец игре!")
        break

    win = vict()
    if win != '':
        data_field()
        print(f"Поздравляем с победой! {win}")
        break


