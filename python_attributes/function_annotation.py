# 定义一个函数
# 参数 num int类型
# 返回值 字符串类型

from typing import Iterator
from typing import Callable


def num_fn(num: int) -> str:  # 有返回参数的类型用"->"
    return str(num)


fn1 = num_fn(100)
print(fn1)

# 定义函数 两个参数都是int 返回int


def sum_fun(a: int, b: int) -> int:
    return a+b


print(type(sum_fun(100, 200)))

# 定义函数参数添加默认值
# num2有默认值 默认值用=表示


def fun_test(num1: int, num2: float = 12.45) -> float:
    return (num1+num2)


print(fun_test(100, 20))  # 不取默认值
print(fun_test(100))


print('-'*10, "定义变量", '-'*10)
# 定义变量 指向一个自定义函数
# 变量指向sum_fun函数 此函数里的参数是[int,int] 返回值是int
f: Callable[[int, int], int] = sum_fun
print(f(100, 200))  # 直接调用f 因为f指向sum_fun这个函数

# 定义一个函数 这个函数产生整数的生成器，每次返回一个
# 生成器其实是一个iterator


def return_fun(num: int) -> Iterator[int]:  # iterator[int] 因为要返回一个产生整数的迭代器
    i = 0
    while i < num:
        yield i  # 每次返回一个
        i += 1
        print(i)


a = return_fun(10)
a.__next__()
a.__next__()
a.__next__()
a.__next__()
a.__next__()
a.__next__()
# print(return_fun(10))


def return_fun1(num: int) -> Iterator[int]:  # iterator[int] 因为要返回一个产生整数的迭代器
    i = 0
    while i < num:
        yield i  # 每次返回一个
        i += 1


for i in return_fun1(10):
    print(i)
