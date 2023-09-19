from dataclasses import dataclass, field
from typing import List
from collections import defaultdict
from typing import ClassVar


@dataclass
class Player:  # define the variable in order
    name: str
    position: str
    age: int


# 创建实例对象
# p = Player('jojo', 'paris', 24)
# print(p)


@dataclass
class Player1:
    name: str
    position: str
    age: int
    # gender: str = field(default='x', repr=False)
    msg: str = field(default_factory=str)
    gender: str = field(default_factory=str)
    # gender: str = field(default='x', repr=True)
    # 类变量
    country: ClassVar[str]


p1 = Player1('jojo', 'Paris', 25)

# print(p1)
print(p1.name)
print(p1.age)
print(p1.msg)
Player1.country = 'China'  # 初始化类变量
print('Class attribute:', Player1.country)   # 类对象进行调用


@dataclass
class Myclass:
    my_list: List[int] = field(default_factory=list)
    my_dict: dict = field(default_factory=lambda: defaultdict(int))


# Usage
obj1 = Myclass()
print(obj1.my_list)

obj2 = Myclass([1, 2, 3], {'a': 1, 'b': 2, 'c': 5})
print(obj2.my_list)
print(obj2.my_dict)
