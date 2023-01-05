matrix = [
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6]
]

print("   | 1 | 2 | 3 | 4 | 5 | 6 |")
print(" 1 | ■ | ■ | ■ | - | - | - |")
print(" 2 | - | - | - | - | ■ | ■ |")
print(" 3 | - | - | - | - | - | - |")
print(" 4 | ■ | - | ■ | - | ■ | - |")
print(" 5 | - | - | - | - | ■ | - |")
print(" 6 | ■ | - | ■ | - | - | - |")

# for i in range(0, len(matrix)):
#     for j in range(0, len(matrix[i])):
#         print(matrix[i][j], end=' ')
#     print()

# обход по элементам
#
# for i in matrix:
#     for j in i:
#         print(j, end=' ')
#     print()

# обход по индексам
# def board():
#
#     print("  1 2 3 4 5 6")
#     count = 1
#     for i in range(6):
#         print(f"{count} ", end='')
#         count += 1
#         for j in range(6):
#             print(j, end=' ')
#         print()
#
# print(matrix[5][4])
# matrix[5][4] = 'O'
# board()
#


