import re
# 贪婪模式 - 尽量多的取匹配
print('-'*10, '贪婪模式', '-'*10)
info = '<div>python</div><div>mysql</div>'
m1 = re.match('<div>.*</div>', info)  # 中间不论有什么内容都给我匹配出来
print(m1)

# 非贪婪模式
print('-'*10, '非贪婪模式', '-'*10)
m2 = re.match('<div>.*?</div>', info)
print(m2)
