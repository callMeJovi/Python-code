import re

# 1. match(pattern,string) 从一个字符串头开始匹配 pattern:正侧表达式规则  string:要匹配的字符串
m1 = re.match('foo', 'food')
print(m1)
m2 = re.match('foo', 'seafood')
print(m2)

# 2. search(pattern,string) 从任意位置开始匹配
# pattern:正侧表达式规则  string:要匹配的字符串
# 返回值: 匹配到的对象 如果没有匹配到返回none
f1 = re.search('foo', 'seafood')
print(f1)
