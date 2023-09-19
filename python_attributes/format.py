name = "joni"
age = 18
print("name:{},age:{}".format(name, age))

print(f'name:{name},age:{age}')
names = ["java", 'python', 'front-end']
print(f'language1:{names[0]},language2:{names[1]}')

a = 10
b = 20
print(f"sum a and b:{a+b}")

print('-'*10, "f-string 使用等号", '-'*10)
a1 = 10
b1 = 20
print(f'{a1=},{b1=}')

# 使用指定字符填充
print('-'*10, "使用指定字符填充", '-'*10)
# 20 使用*居中显示
title = 'python dev'
print('{:*^20}'.format(title))
print(f'{title:*^20}')

# 居右显示 20个字符
print(f'{name:*>20}')

# 居左显示 20个字符
print(f'{name:*<20}')

# 对数值变量的格式化
price = 12.345
print('{:.2f}'.format(price))  # 保留两位小数
print(f'{price:.2f}')

num = 12
print(f'{num=:.1f}')

pct = 0.789
print('{:.2f}%'.format(pct*100))
print(f'{pct*100:.0f}%')
