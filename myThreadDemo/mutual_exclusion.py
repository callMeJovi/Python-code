"""
互斥锁案例
"""
from threading import Thread, Lock
from time import sleep


class Account:
    # initialize bank account
    def __init__(self, money, name):
        self.money = money
        self.name = name

# 模拟提款操作


class Withdraw(Thread):
    # 创建构造函数 param 取多少钱 在哪个账户上取
    def __init__(self, howMuch, acc):
        Thread.__init__(self)

        self.howMuch = howMuch
        self.acc = acc
        self.expenseTotal = 0

    def run(self):
        lock1.acquire()  # 把锁加上
        if self.acc.money < self.howMuch:
            print('余额不足')
            return
        sleep(1)  # 等待判断完可以取钱 那么阻塞 为了测试发生冲突问题
        # print(self.acc.money)
        self.acc.money = self.acc.money-self.howMuch
        self.expenseTotal = self.expenseTotal+self.howMuch
        lock1.release()  # 把锁释放
        print(f"账户:{self.acc.name},余额:{self.acc.money}")
        print(f"账户:{self.acc.name},共提取:{self.expenseTotal}")


if __name__ == "__main__":
    a1 = Account(1000, "jojo")
    lock1 = Lock()  # 创建锁对象
    withdraw1 = Withdraw(80, a1)  # thread 1 to withdraw money: me
    withdraw2 = Withdraw(80, a1)  # thread 2 to withdraw money: my bf
    withdraw1.start()
    withdraw2.start()
