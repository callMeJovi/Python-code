# 简单类型变量标注
# a: int = 10
# b: str = "hello"
# c:float=3.14
# d:bool=True
# e:bytes=b

# 复杂类型变量标注
from typing import List, Set, Dict, Tuple
# define a list 列表 with integer in it
x: List[int] = [1, 3, 4]

# set 集合
y: Set[str] = {'ab', 'cd', 'ef'}

# 定义字典
z: Dict[str, int] = {"age": 18, "income": 180000}
# 用object就可以兼容int和str
z1: Dict[str, object] = {"age": 18, "income": 19000, "name": 'jojo'}

# 定义元组 元组是不可更改的
# (3) is wrong. if I want to represent only 1 element, it must be (a,)
t: Tuple[int] = (3,)
# if I want to represent 3 elements, then it must be 3 int in Tuple =>Tuple[int,int,int]
# 对于元组来说 元素的多少和类型对应
t1: Tuple[int, int, int] = (3, 2, 4)
t2: Tuple[int, str, float] = (3, 'jo', 6.325)
print(t2)

# To define Tuple with flexible size, use "..."
t3: Tuple[int, ...] = (1, 2, 3, 4)  # 元组的大小可变

# python3.10新特性中已存在list tuple dict set 不需要导入typing也可直接用
# 变量后面加类型
# x: list[str] = ['a', 'b', 'c']
# x:tuple[int]=(2,)
# x: tuple[int, int] = (2, 3)
# x: tuple[int, ...] = (1, 2, 5, 9)
# x: set[str] = {'aa', 'bb', 'cc'}
# x: dict[str, object] = {'name': 'jojj', 'age': 18,'k3':True}
