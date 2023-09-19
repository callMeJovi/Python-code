"""
一个函数不止有他的执行语句，还有着 __name__（函数名，__doc__ （说明文档）等属性，我们之前的例子会导致这些属性改变。
functool.wraps可以将原函数对象的指定属性赋值给包装函数对象，默认有module、name、doc，或者通过参数选择。
"""
from functools import wraps


def mylog(func):
    @wraps(func)  # 用wraps目的是将原函数fun2函数的属性复制出来
    # 如果没有@wraps(func) 那么fun2.__doc__打印的就是包装的内部函数infunc的文档字符串"""包装的内部函数"""
    def infunc(*args, **kwargs):
        """包装的内部函数"""
        print("日志纪录...")
        print("函数文档:", func.__doc__)
        return func(*args, **kwargs)
    return infunc


@mylog  # fun2 = mylog(fun2)
def fun2():
    """强大的功能2"""  # 文档字符串可以通过__doc__来访问
    print("使用功能2")


if __name__ == '__main__':
    fun2()
    print("函数文档--->", fun2.__doc__)
