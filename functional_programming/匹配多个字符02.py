import re

# * 匹配0次或无限次
print('-'*10, '*符号的使用', '-'*10)
m1 = re.match('h', 'hello')
m2 = re.match('h*', 'hello')  # ello匹配不了但h可以匹配 即使有* 代表匹配一次或无数次
print(m1)
print(m2)
m3 = re.match('\w*', 'hello')  # \w代表字母数字下划线
print(m3)
m4 = re.match('\w*\s\w*', 'hello world')
print(m4)
m5 = re.match('\s\w*\s\w*', ' hello world')
print(m5)
# span=(0, 1), match=' ' 因为\s代表匹配一次空格
m6 = re.match('\s\w*', ' \thello world')
print(m6)
# \s*意思是无论多少个空格都给我匹配上
m7 = re.match('\s*\w*', ' \thello world')
print(m7.group())
m8 = re.match('[\s\w]*', ' \thello world')
print(m8.group())

# + 匹配1次或无限次
print('-'*10, '+符号的使用', '-'*10)
# start with p, end with n; .means any character;
n1 = re.match('p.+n', 'python')
print(n1)
n2 = re.match('p.+n', 'pn')
print(n2)

# ? 匹配0次或1次
print('-'*10, '?符号的使用', '-'*10)
n3 = re.match('http?', 'httpp')
print(n3)
n4 = re.match('https?', 'http')
print(n4)

# {n} 匹配n次
print('-'*10, '{n} 符号的使用', '-'*10)
n5 = re.match('\w{2}', 'python')
print(n5)

# {n,} 匹配n次或无限次
print('-'*10, '{n,} 符号的使用', '-'*10)
n6 = re.match('\w{1,}', 'python')
print(n6)

# {,m} 匹配0次到m次
print('-'*10, '{,m} 符号的使用', '-'*10)
n7 = re.match('\w{,3}', 'python')
print(n7)

# {n,m} 匹配n次到m次
print('-'*10, '{n,m} 符号的使用', '-'*10)
n8 = re.match('\w{1,3}', 'python')
print(n8)

# ^ 匹配开头 - 以...开头
print('-'*10, '^ 符号的使用', '-'*10)
# ^\d 以数字开头  . 意思是后面接的字符是什么无所谓所以可以是任意字符串  +匹配多次
f1 = re.match('^\d.+', '67hello')
print(f1)

# $ 匹配结尾 - 以...结尾
print('-'*10, '$ 符号的使用', '-'*10)
f2 = re.match('^\d.+\d$', '67hello7')
print(f2)
f3 = re.match('^\d.+\d', '67hell7o')
print(f3)

# []代表 列举出内容可以是哪些 也就是枚举
# [^指定字符] 表示除了指定字符都匹配
print('-'*10, '[^]取反功能 ', '-'*10)
f4 = re.match('[^hello]*', '67hello7')
print(f4)
