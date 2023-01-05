from datetime import datetime
from time import perf_counter
def timer():
    start = perf_counter()

    def inner():

        t1 += perf_counter() - start
        t2 = perf_counter() - t1
        return t2

    return