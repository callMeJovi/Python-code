# 本次内容，是装饰器的基础
# every time we add a new feature to the function, we can use closure
from time import sleep


def fun1():
    print("feature 1")


def fun2(a, b, c):  # *args,**kwargs when parameters needed
    print("feature 2", a, b, c)


def outfunc(func):
    def infunc(*args, **kwargs):  # *args,**kwargs when parameters needed
        print("journal starts...")
        sleep(3)
        func(*args, **kwargs)  # *args,**kwargs when parameters needed
        print("journal ends...")

    return infunc


# newFeature = outfunc(fun1)  # don't need call fun1()
# newFeature()
# print('-----------')
# print(id(fun1))
fun1 = outfunc(fun1)  # or call once, we'll have all the features
# print(id(fun1))
fun1()
# no need to modify the fun2,juste assigne the output of outfun to fun2
fun2 = outfunc(fun2)
fun2(1, 2, 3)
