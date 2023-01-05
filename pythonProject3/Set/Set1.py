abons = {"Иванов", "Петров", "Сидоров", "Юркин"}
debtors = {"Петров", "Юркин"}
non_debtors = abons.difference(debtors)
print(non_debtors)