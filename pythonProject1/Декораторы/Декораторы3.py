import time


def decorator_time(fn):
   def wrapper():
       print(f"Запустилась функция {fn}")
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
       print(f"Функция выполнилась. Время: {dt:.10f}")
       return dt  # задекорированная функция будет возвращать время работы
   return wrapper


def pow_2():
        return 10000000 ** 2


def in_build_pow():
        return pow(10000000, 2)




N = 100

mean_pow2 = 0
mean_in_build_pow = 0
for i in range(N):
    mean_pow2 += pow_2()
    mean_in_build_pow += in_build_pow()

pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

pow_2()