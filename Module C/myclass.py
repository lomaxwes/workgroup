# class MyClass():
#     def f(self):
#         return 155
#
#
# if __name__ == "__main__":
#     mc = MyClass()
#     print("It's only for test", mc.f())


# Теперь немного модернизируем код для наглядности:

class MyClass():
   def f(self):
       return 155
mc2=MyClass()
print("It's for test too", mc2.f())

if __name__ == "__main__":
   mc=MyClass()
   print("It's only for test", mc.f())