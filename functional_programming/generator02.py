"""
生成器函数的创建 生成器本质
1. 函数有了yield之后，调用它，就会生成一个生成器
2. yield作用：程序挂起，返回相应的值。下次从下一个语句开始执行。
3. return在生成器中代表生成器终止，直接报错：StopIeratation
4. next方法作用：唤醒并继续执行
"""


def test():
    print("start")
    i = 0

    while i < 3:
        # yield i
        print(i)
        temp = yield i  # 下一个语句不等于下一行 这里yield i的下一行语句是temp
        print(f"temp:{temp}")
        print(f'i: {i}')
        i += 1
    print("end")
    return "done"  # 生成器遇到return就会终止


if __name__ == "__main__":
    a = test()
    print(a)  # generator object because of yield
    a.__next__()  # when come across "yield", execution stopped at yield, the value of i is returned at same time
    print('0------------0')
    a.__next__()  # second time call the fn, the fn will be executed from where the execution has been stopped 从挂起的地方开始执行
    # # 所以打印i=0 then i=i+1 then enter into while loop => run into yield => execution stopped at yield
    print('1-------------1')
    a.__next__()  # third time call the fn, i=1
    print('2-------------2')
    a.__next__()
