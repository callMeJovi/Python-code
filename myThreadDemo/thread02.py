# coding=utf-8
"""
类包装创建线程
"""
from threading import Thread
from time import sleep


class MyThread(Thread):
    # 构造函数
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"线程{self.name},start")
        for i in range(3):
            print(f"线程{self.name},{i}")
            sleep(3)
        print(f"线程{self.name},end")


if __name__ == '__main__':
    print("主线程,start")
    # 创建线程
    t1 = MyThread("t1")
    # t2 = MyThread("t2")
    # t1设置为守护线程
    t1.daemon = True
    # 启动线程
    t1.start()  # 当调用start时 线程启动 会自动调用run方法
    # t2.start()

    print("主线程, end")
