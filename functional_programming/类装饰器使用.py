"""
上面写的装饰器都是函数来完成的。我们用类也可以实现装饰器。
类能实现装饰器的功能， 是由于当我们调用一个对象时，实际上调用的是它的 __call__ 方法。
"""

from typing import Any


class Demo:
    def __call__(self):
        print('我是 Demo')


demo = Demo()
demo()  # 直接调用对象，实质是调用了他的__call__()


# 类装饰器


class MyvlogDecorator():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("my vlog processing...")
        return self.func(*args, **kwargs)


@MyvlogDecorator  # fun2=MyvlogDecorator(fun2)
# 将fun2传入类中 那么fun2就变成参数指向init中的func参数
# 当调用类时 类将创建的对象给了fun2 那么fun2就变成了类的对象不再是fun2函数了
# 那么在if name里调fun2时 其实就是调用类myvlog的对象 也就是调用对象的方法__call__
def fun2():
    print("feature 2...")


if __name__ == "__main__":
    fun2()
