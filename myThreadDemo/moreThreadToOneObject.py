"""
多了线程访问同一个资源
"""
# 未使用线程同步和互斥锁的形况
from threading import Thread
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
        if self.acc.money < self.howMuch:
            return
        sleep(1)  # 等待判断完可以取钱 那么阻塞 为了测试发生冲突问题
        # print(self.acc.money)
        self.acc.money = self.acc.money-self.howMuch
        self.expenseTotal = self.expenseTotal+self.howMuch
        print(f"账户:{self.acc.name},余额:{self.acc.money}")
        print(f"账户:{self.acc.name},共提取:{self.expenseTotal}")


if __name__ == "__main__":
    a1 = Account(100, "jojo")

    withdraw1 = Withdraw(80, a1)  # thread 1 to withdraw money: me
    withdraw2 = Withdraw(80, a1)  # thread 2 to withdraw money: my bf
    withdraw1.start()
    withdraw2.start()
