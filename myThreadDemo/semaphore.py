"""
信号量的使用案例
一个object资源只能被几个线程访问 
一个房子只能允许两个人进来
"""
from threading import Semaphore
from threading import Thread
from time import sleep

# name 房子名字 se信号量


def home(name, se):
    se.acquire()  # get se
    print(f"{name} enters into the room")
    sleep(3)
    print(f"****{name} step out of the room")
    se.release()


if __name__ == "__main__":
    se = Semaphore(2)  # 信号量对象 最多只能有两个人进来房间
    for i in range(7):  # 创建7个线程
        t = Thread(target=home, args=(f"jojo{i}", se))
        t.start()
