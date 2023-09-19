# coding=utf-8
# 需求：实现变量a 自增
# 通过全局变量，可以实现，但会污染其他程序
a = 10


def add():
    a = 10
    a += 1
    print("a:", a)


def print_ten():
    if a == 10:
        print("ten!")
    else:
        print("global variable a is not equal to 10")


add()
add()
add()
print_ten()
