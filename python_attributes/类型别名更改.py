# 旧版本
from typing import TypeAlias
oldstr = str  # 将str字符串类型赋值给变量oldstr
# 用变量oldstr给其他变量进行标注
msg: oldstr = "helloworld"
print(msg)

# new version
newstr: TypeAlias = str  # 变量后面接typeAlias，变量newstr就不再是变量名而是类型别名
newint: TypeAlias = int


def func_test(num: newint, msg: newstr) -> newstr:
    return str(num)+msg


print(func_test(10, 'file'))
