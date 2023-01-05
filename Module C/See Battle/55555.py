# if a := int(input("Введите число: ")) < 1:
#     print("dfg")
# else:
#     print("Заново")


# pr += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
#             for i, row in enumerate(self.field):
#                 pr += f"\n{i+1} | " + " | ".join(row) + " |"


a = [ 'abcd' for i in range(4)]

for i, j in enumerate(a):
    print(f"{i+1} '" + "' '".join(j) + "' ")