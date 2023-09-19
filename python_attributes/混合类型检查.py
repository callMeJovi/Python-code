# 联合运算符使用 "|" 来代替旧版本中union方法 使程序更加简洁
# 旧版本
from typing import Union


def old_func_test(num: Union[int, float]) -> Union[int, float]:
    return num+100


print(old_func_test(100.12))

# new版本


def old_func_test1(num: int | float) -> int | float:
    return num+100


print(old_func_test1(100.12))
