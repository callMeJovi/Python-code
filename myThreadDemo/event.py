"""
event事件的使用案例
"""
import threading
import time


def hotpot(name):
    # 等待事件，进入等待阻塞状态
    print(f"{name}已经启动")
    print(f"{name}已经进入就餐状态")
    time.sleep(1)
    event.wait()  # 使用事件对象
    print(f"{name}收到通知")
    print(f"{name}开始吃咯")


if __name__ == "__main__":
    # 创建事件对象
    event = threading.Event()
    # 创建新线程
    thread1 = threading.Thread(target=hotpot, args=("jojo",))
    thread2 = threading.Thread(target=hotpot, args=("gigi",))
    thread1.start()
    thread2.start()

    time.sleep(10)
    # 发送事件通知
    print('----->>>主线程通知小伙伴开吃')
    event.set()
