
# Создадим ещё один отдельный файл под названием testRectangle.py для того, чтобы реализовать наследование.
# Причём обязательно в той папке, где находится rectangle.py(в нашем случае это папка Module C).

from rectangle import Rectangle

r1 = Rectangle(10, 5)
r2 = Rectangle(2, 3)

print("r1.width =", r1.width)
print("r1.height =", r1.height)
print("r1.get_width =", r1.get_width())
print("r1.get_height =", r1.get_height())
print("r1.get_area =", r1.get_area())

print("r2.width =", r2.width)
print("r2.height =", r2.height)
print("r2.get_width =", r2.get_width())
print("r2.get_height =", r2.get_height())
print("r2.get_area =", r2.get_area())