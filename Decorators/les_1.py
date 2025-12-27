from typing import Callable
import time


def deco(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print(f" time: {stop - start}")
        return res
    return wrapper

@deco
def my_func(time_sleep: int):
    time.sleep(time_sleep)
    return 123

my_func(1.5)

# Декщратор с парраметром

