# 多个装饰器的执行顺序
from time import sleep
import time


def mylog(func):
    print("mylog start")

    def infunc1():
        print("日志记录 start...")
        func()
        print("日志记录 end...")
    print("mylog ends")
    return infunc1


def cost_time(func):
    print("cost time starts...")

    def infunc2():
        print("chrono starts...")
        start = time.time()
        func()
        end = time.time()
        print(f"time spent: {end-start}")
    print("cost time ends...")
    return infunc2


@mylog
@cost_time
def fn2():
    print("fun2, start")
    sleep(3)
    print("fun2, end")


fn2()
