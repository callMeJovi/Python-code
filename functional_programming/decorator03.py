# decorator with param

def mylog(type):  # 此处参数是针对@mylog("excel")
    def decorator(func):
        def infunc(*args, **kwargs):  # 此处参数是对于执行函数fun2
            if type == "excel":
                print("In excel: myVlog...")
            else:
                print("In consol: myVlog....")
            func(*args, **kwargs)

        return infunc

    return decorator


@mylog("excel")
def fun2(a, b):
    print("feature 2", a, b)


if __name__ == '__main__':
    fun2(100, 200)
