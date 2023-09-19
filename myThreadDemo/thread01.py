# coding=utf-8
"""
方法模式创建线程
"""
from threading import Thread
from time import sleep


def func1(name):
    print(f"线程{name},开始")
    for i in range(3):
        print(f'线程:{name},{i}')
        sleep(1)

    print(f"线程{name},结束")


# determine if the module works as a separated module 判断是否作为独立模块运行
# 如果作为独立模块 if statement会被运行 如果作为导入模块则不会运行if后的代码
if __name__ == '__main__':
    # when executing a module, system will start a main threading by default
    print("主线程, start...")
    # creat threads
    # 2 params: target=> execute the selected fn when starting the thread; args=> tuple
    # t1 = Thread(target=func1("t1"))  # args=("t1", "t11")
    # t2 = Thread(target=func1("t2"))  # args=("t2", "t22")
    t1 = Thread(target=func1, args=("t1",))
    t2 = Thread(target=func1, args=("t2",))
    # start up threads
    t1.start()
    t2.start()
    # 主线程会等待t1 t2结束后在往下执行
    t1.join()
    t2.join()
    print("主线程, end...")

# 三个线程互补影响
