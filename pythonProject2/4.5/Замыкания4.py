from datetime import datetime
from time import perf_counter
def timer():
    start = perf_counter()

    def inner():

        return perf_counter() - start
    return inner

t = timer()

print(t())
print(t())
print(t())
