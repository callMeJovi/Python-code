# coding=utf-8
# 需求：实现变量a 自增
# 通过闭包，也没有污染全局变量a。也实现了自增
a = 10


def add():
    a = 10  # 自由变量
    print(a)

    def increment(age):  # because of closure, a became 自由变量
        nonlocal a  # declare nonlocal a to be able to modify the a
        # 闭包是由于函数内部使用了函数外部的变量。这个函数对象不销毁，则外部函数的局部变量也不会被销毁！
        a += 1
        print(f"my age:{age}")
        print("a:", a)
    return increment


def print_ten():
    if a == 10:
        print("ten!")
    else:
        print("全局变量a, 不等于10")


inner = add()  # the result of executing the add() function is given to inner
# fn add() execute => increment() not executable because it isn't called => retunr increment => assigne the increment
# to inner => inner() being called => increment() being called and executed
# inner =add # means give inner the object
print('----------------')
inner(20)
inner(22)
inner(25)

print_ten()
