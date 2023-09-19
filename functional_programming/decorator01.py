def mylog(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print("journal...")
    return inner


@mylog  # fn1 = mylog(fn1)
def fn1(a, b):
    print("feature 1", a, b)


@mylog  # fn2 = mylog(fn2)
def fn2():
    print("feature 2")


# fn1 = mylog(fn1)
# fn2 = mylog(fn2)
fn1(100, 200)
fn2()
