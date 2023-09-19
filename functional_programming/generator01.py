L = [x*x for x in range(10)]
print(L)
g = (x*x for x in range(10))
print(g)
print(g.__next__())
print(g.__next__())
