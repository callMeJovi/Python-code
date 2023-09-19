"""
Regular expression =regex  正则表达式
*	匹配前一个字符出现0次或者无限次，即可有可无
+	匹配前一个字符出现1次或者无限次，即至少有1次
?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}	匹配前一个字符出现m次
{m,n}	匹配前一个字符出现从m到n次
"""
import re
re1 = re.match("[A-Z][a-z]*", "M")
print(re1.group())

re2 = re.match("[A-Z][a-z]*", "MnnM")  # *在谁后面就代表那个字符可以出现多少次 这里代表[a-z]
print(re2.group())

re3 = re.match("[A-Z][a-z]*", "Aabcdef")  # *将所有的小写都匹配出来因为星号就是可以匹配多次的意思
print(re3)

# + 匹配前一个字符出现1次或者无限次，即至少有1次
re4 = re.match("py.+n", "python")
print(re4)

# ? 0 or 1
re5 = re.match('https?', 'http')  # ?是针对?前的一个字符是否存在 也就是说最后一个字符可有可无
print(re5)

# {m} {m,n} 匹配m次也就是说前m个字符
re6 = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")  # 前六个
print(re6.group())

re7 = re.match("[a-zA-Z0-9_]{8,20}", "1a2b3c4d5e6f7g8h9ijklmn")  # 前20个
print(re7.group())

re8 = re.match("[0-9A-Za-z]{6}", "12a3g45678")
print(re8)
