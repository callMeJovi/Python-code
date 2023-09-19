"""
生产者和消费者
"""
from queue import Queue
from time import sleep
from threading import Thread


def producer():
    num = 1
    while True:  # keep producing
        if queue.qsize() < 5:  # 缓冲区size 缓冲区可以放多少个对象
            print(f"生产包子{num}")
            queue.put(f"包子:{num}")
            num += 1
        else:
            print("包子满了 等待消费")
            break
        sleep(1)


def consumer():
    while True:
        if queue.qsize() <= 0:
            print("没有库存了")
            break
        else:
            print(f"获取包子:{queue.get()}")
        sleep(1)


if __name__ == "__main__":
    queue = Queue()  # define a buffer zone 缓冲区
    t1 = Thread(target=producer)
    t2 = Thread(target=consumer)
    t1.start()
    t1.join()
    t2.start()
