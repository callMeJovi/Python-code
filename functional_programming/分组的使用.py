import re
# | 或者的使用
print('------------------| 或者---------------')
skill_list = ['python', 'mysql', 'flask', 'django']
for value in skill_list:
    m1 = re.match('mysql|flask|python', value)
    # m1 = re.match('mysql|flask', value)
    print(m1)

# () 分组的使用
# 匹配邮箱 查看邮箱格式是否符合要求 163,126,qq
print('------------------()分组---------------')
# 不能直接用. 因为.可以匹配任意字符 如果163#com那就不符合要求
m2 = re.match('\w{4,20}@(163|126|qq)\.com', 'hello@163.com')
# \转义字符
print(m2)

# 提取电话号码 提取分组数据时从1开始
print('------------------通过分组提取数据---------------')
m3 = re.match('(.+):(\d*)', '电话:10086')
# m3 = re.match('.+:(\d{4,10})', '电话:10086')
print(m3.group(1))
print(m3.group(2))

# \num 的使用
# 需求：匹配出<html>python</html>
print('------------------num 的使用---------------')
info = '<html>python</html>'  # div, h1,h2...h6, span, title, p
m4 = re.match('<[a-z1-6]+>(.*)</[a-z1-6]+>', info)
print(m4.group(1))
m5 = re.match('<([a-z1-6]+)>(.*)</\\1>', info)
# \\1 : 1 indicates the first group () of the string =>[a-z1-6]+
# second group => .*
# we use \1 to indicate the similarity to the first group and not to repeat it.
print(m5.group(1))
print(m5.group(2))

# 正则表达式起名 用于简化\num 如果字符过长就不用去数
print('------------------?P<name> 的使用---------------')
m6 = re.match('<(?P<name1>[a-z1-6]+)>(.*)</(?P=name1)>', info)
print(m6.group(1))
print(m6.group(2))


# 标志的使用
print('------------------标志的使用---------------')
print('------------------re.I 的使用---------------')
# 忽略大小写 re.I
re1 = re.match('[a-z]+', 'Hello', re.I)
# re1 = re.match('[a-z]+', 'Hello', re.IGNORECASE)
print(re1.group())

print('------------------re.S 的使用---------------')
# 可以匹配所有字符,包含换行符 re.S
re2 = re.match('.+', 'Hello\nPython', re.S)
print(re2.group())

print('------------------re.X 的使用---------------')
# 忽略空格和注释,使正则表达式更具有可读性
re3 = re.match('''
   ^   # 行的开头
   (   # 分组1开始
   [a-z]+[A-Z]*  # 字母开头,可以有大写字母
   |             # 或者
   [A-Z]+[a-z]*  # 大写字母开头,可以有小写字母
   )       # 分组1结束
   \s+     #空格
   (Python)  #分组2
''', 'Hello Python', re.X)
print(re3.group())
