def test():
    print("test function is running")


def test03(a, b):
    print(f"test03,{a},{b}")


def test2(f):
    f(2, 3)
    print("test2 function is running")


test2(test03)
