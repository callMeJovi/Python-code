from functools import reduce


def f(a):
    return a*a


b = []
for n in range(9):
    b.append(f(n))
print(b)
print('---------------------')

L = map(f, range(1, 9))
print(list(L))

L = map(lambda n: n*n, range(1, 9))
print(list(L))


def f(x, y):
    return x+y


L = map(f, [1, 2, 3, 4, 5], [20, 30, 40])
print(list(L))

# L=map(lambda x,y:x+y,[1,2,3,4],[10,20,30])
# print(list(L))


def add(x, y):
    return x+y


sum = reduce(add, [1, 3, 5, 7, 9, 10])
print(sum)

# --------------------------------
# 在一个list中，删掉偶数，只保留奇数


def is_odd(n):
    return n % 2


L = filter(is_odd, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(list(L))

# determine if there're empty string
# def not_empty(str):
#     return str and str.strip()


def not_empty(str):
    if str and str.strip():
        return str


L = filter(not_empty, ["qsf", "kkk", "jljl ", None, 0,  "", " "])
print(list(L))


# k = ""


# def istrue():

#     if k.strip():
#         print("yes")


# istrue()
