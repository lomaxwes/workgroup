bodycount = {
    'Проклятие черной жемчужины': {
        'человек': 17
    },
    'Сундук мертвеца': {
        'человек': 56,
        'раков отшельников': 1
    },
    'На краю света': {
        'человек': 88
    },
    'На странных берега': {
        'человек': 56,
        'русалок': 2,
        'ядовитых жаб': 3,
        'пиратов зомби': 2
    }
}


dead = 0
# for val in bodycount.values():
#     for val2 in val.values():
#         dead += val2
#         # print(n)
#
# print(f" Количество погибших: {dead}")


for val in bodycount.values():
    dead += sum(val.values())
print(f" Количество погибших: {dead}")