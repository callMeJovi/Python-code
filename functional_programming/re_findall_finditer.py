"""
re.findall, re.finditer, re.sub
"""
import re
# 1. findall(patter,string) 从字符串中查找所有符合正则表达式的数据
# pattern:正侧表达式规则  string:要匹配的字符串
# 匹配到数据后，返回一个列表 列表中存放的是匹配到的数据
# 如果没有匹配到数据 返回一个空列表
f1 = re.findall('ab', 'abc')
print(f1)
f2 = re.findall('ef', 'abcd')
print(f2)  # return empty array (list)
f3 = re.findall('ab', '1abcabcabc0')  # 3 'ab' were found
f4 = re.findall('ab', '1a6bcab7c9abc0')
print(f3)
print(f4)

# 2. finditer(patter,string) 从字符中查找所有符合正则表达式的数据
# 返回的结果是个迭代器 迭代器中存放的是匹配到的数据
fi1 = re.finditer('ab', '1a6bcab7c9abc0')
print(fi1)
for i in fi1:
    print(i.group())

fi3 = re.finditer('ab', '1abcabcabc0')
print(fi3)
for i in fi3:
    print(i)

# 3. re.sub(pattern,repl,string) 不会替换原有的字符串text for example
# pattern:正则表达式 repl:要替换的字符串 string:要匹配的字符串
text = "I'm a software developer at google,at Meta, at, at"
text1 = re.sub('at', 'AND', text)
print(text1)
