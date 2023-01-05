shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])
print(list_id_before)
shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])
print(list_id_after)


print(list_id_before is list_id_after)
print(shopping_center)