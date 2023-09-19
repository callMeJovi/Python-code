import time
from typing import Any

"""
用类方法实现缓存装饰器 important !!!
"""


class CacheDecorator():
    __cache = {}

    def __init__(self, func):
        self.func = func

    def __call__(self, *args: Any, **kwds: Any):
        # 如果缓存中有对应的方法名，则直接返回对应的返回值
        if self.func.__name__ in CacheDecorator.__cache:
            return CacheDecorator.__cache[self.func.__name__]
        # 如果缓存中没有对应的方法名，则进行计算，并将结果缓存
        else:
            result = self.func(*args, **kwds)
            CacheDecorator.__cache[self.func.__name__] = result
            return result


def chrono(func):
    def take_time(*args, **kwds):
        start = time.time()
        result = func(*args, **kwds)
        end = time.time()
        print(f"the execution time: {end-start}")
        return result
    return take_time


@chrono
@CacheDecorator
def func1_long_time():  # can pass param
    """
    模拟耗时较长 每次执行返回结果都一样的情况
    """
    print("start func1")
    time.sleep(5)
    print("end func1")
    return 999


if __name__ == "__main__":
    r1 = func1_long_time()
    print(r1)
    r2 = func1_long_time()
    print(r2)


# fun1 = func1_long_time()
# print(fun1)
