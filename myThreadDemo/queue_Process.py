"""
使用queue实现进程间的通信
"""
from multiprocessing import Process
from multiprocessing import Queue
from time import sleep


class MyProcess(Process):
    def __init__(self, name, mq):
        Process.__init__(self)
        self.name = name
        self.mq = mq

    def run(self):
        print(f"Process:{self.name}, start")
        print(f"get Data:{self.mq.get()}")
        sleep(3)
        print(f"Process:{self.name}, end")


if __name__ == "__main__":
    # 创建队列对象
    mq = Queue()
    mq.put("1")
    mq.put("2")
    mq.put("3")

    # 创建进程 定义进程列表

    p1 = MyProcess("p1", mq)
    p2 = MyProcess("p2", mq)
    p3 = MyProcess("p3", mq)
    p1.start()
    p2.start()
    p3.start()
