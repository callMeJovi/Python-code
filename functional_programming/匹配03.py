"""匹配单个字符"""
import re
# 精准匹配
print('-'*10, '精准匹配', '-'*10)
m = re.match('test', 'test python re')
print(m)
print(m.group())

# 特殊字符
print('-'*10, '特殊字符', '-'*10)
m1 = re.match('.test', '$test python re')
m2 = re.match('\$test', '$test python re')
print(m1.group())
print(m2.group())

# 匹配字符
print('-'*10, '匹配字符', '-'*10)  # . /d /D
m3 = re.match('.', '$')  # . 匹配任意字符
print(m3)
m4 = re.match('te.t', 'test')
print(m4)

# [] 匹配[ ]中列举的字符
print('-'*10, '匹配字符 []', '-'*10)
m5 = re.match('h', 'hello python')
print(m5)
m6 = re.match('[h]', 'hello python')
print(m6)
m7 = re.match('[hH]', 'Hello python')
print(m7)

# [0123456789] -> if the string starts with number, it can be matched
m8 = re.match('[0123456789]', '6hello python')
print(m8)
m9 = re.match('h[0-9]', 'h9ello python')
print(m9)

m10 = re.match('[a-z]', 'hello python')
print(m10)
m11 = re.match('[a-zA-Z]', 'Hello python')

m12 = re.match('[0-35-9]', '4hello python')
print(m12)

# ---------------------------------
# \d 匹配数字
print('-'*10, '\d匹配数字', '-'*10)
t = re.match('python2', 'python2stops')
print(t)

t2 = re.match('python\d', 'python2stops')
print(t2)

# \D 匹配非数字
t3 = re.match('python\D', 'python*stops')
print(t3)

# \s 匹配空白 空格 tab键
print('-'*10, '\查看是否有空白信息', '-'*10)
t4 = re.match('python\stest', 'python test')
t5 = re.match('python\stest', 'python\ttest')
print(t4)
print(t5.group())

# \S 匹配非空白字符 -> 只要不是空白字符就能匹配上
print('-'*10, '\查看是否有非空白字符', '-'*10)
t6 = re.match('python\Stest', 'python^test')
print(t6)

# \w 匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
print('-'*10, '\匹配单词字符', '-'*10)
t7 = re.match('\w', 'python')
# t7 = re.match('\w', '_python')
# t7 = re.match('\w', '中python')
print(t7)

# \W 匹配非单词字符
print('-'*10, '\匹配非单词字符', '-'*10)
t8 = re.match('\W', '&python')
print(t8)

# 匹配任意数据 [\d\D] [\s\S]
print('-'*10, '\匹配任意数据', '-'*10)
print(re.match('[\d\D]', 'python').group())
print(re.match('[\d\D]', '测试python').group())
