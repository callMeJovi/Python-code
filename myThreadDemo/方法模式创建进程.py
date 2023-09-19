"""
方法模式创建进程
"""
from multiprocessing import Process
import os
from time import sleep


def fun1(name):
    print(f'当前进程的ID:{os.getpid()}')
    print(f'父进程ID:{os.getppid()}')  # get parent process id.
    # sleep(3)
    print(f'Process: {name},start')
    sleep(3)
    print(f'Process: {name},end')


def fun2(name):
    pass


# 如果不加__main__限制的话，就会无限递归创建子进程，进而报错。
if __name__ == "__main__":
    # get process ID. this process is parent process
    print("当前main进程的ID:", os.getpid())
    # create a process
    p1 = Process(target=fun1, args=("t1",))
    p2 = Process(target=fun1, args=("t2",))
    p1.start()
    p2.start()
