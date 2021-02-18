# format(value,format_spec)

# 关键代码段：
from datetime import datetime

print(format(12.2, 'f'))  # 转换成浮点数，默认为小数保留6位
# 12.200000
print(format(81, '8d'))  # 8位整数显示，默认靠右对齐，不足部分整数前用空格填充
#       81
print(format(628, '.1f'))  # 格式化为保留1位小数的浮点数
# 628.0
print(format(0.161896, '%'))  # 将小数格式化成百分数，默认保留6位小数
# 16.189600%
print('$' + format(1201398.2315, '.2f'))  # 添加美元符号，小数保留2位
# $1201398.23
print(format('PYTHON', 'M^20.3'))  # 截取3个字符，宽度为20居中，不足用“M”填充
# MMMMMMMMPYTMMMMMMMMM
print(format(0X5A, 'x'))  # 十六进制数5A转换成十进制数，“0X”代表十六进制数
# 90

# format_spec ::= [[fill]align][sign][#][0][width][,][.precision][type]
# 填充、对齐方式、正号、进制标志、宽度、千位符号、精度、输出类型
print(format(81, '@<10'))  # 向左对齐，不足10位用@填充
s = 'PYTHON'
print(format(s, '10'))  # 字符串默认向左对齐
# PYTHON
print(format(81.23, '10'))  # 数字默认向右对齐
#     81.23
print(format(s, '0>10'))  # 向右对齐，左侧用0填充
print(format(s, '>010'))  # 与上一行代码运行结果相同
# 0000PYTHON
print(format(s, '@^10'))  # 居中对齐，两侧用@填充
# @@PYTHON@@
print(format(-81.23, '0=10'))  # 在符号位后填充0，=只对数字有效
# -000081.23
print(format(+81.23, '0=10'))  # 注意 正号的情况
# 0000081.23
print(format(81.23, '0=+10'))
# +000081.23

print(format(21389, '#x'))  # 输出整数的小写十六进制方式，#是显示进制符号
# 0x538d
print(format(21389, 'x'))  # 输出整数的小写十六进制方式
# 538d

print(format(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")))
now = datetime.now()
wx = datetime.now().date()
print(format(now, '%Y-%m-%d %H:%M:%S %Z'))
print(now)
print(wx)

nba = {1: '伦纳德', 2: '哈登', 3: '乔治'}
for key, value in nba.items():
    print(format(key, '0>6'), "====>", value)

for i in range(65, 69):
    for j in range(1, 6):
        data = format(i, 'c') + format(j, '>05') + " "
        print(data, end="")
    print()

print(format(81, " f"))  # 空格表示在正数前加空格，在负数前加-；
print(format(-81, " f"))
#  81.000000
# -81.000000

print(format(3.1415926535898, 'e'))
print(format(3.1415926535898, 'E'))
print(format(3.1415926535898, 'f'))
print(format(3.1415926535898, 'F'))
print(format(3.1415926535898, 'g'))
print(format(3.1415926535898, 'G'))

# 3.141593e+00
# 3.141593E+00
# 3.141593
# 3.141593
# 3.14159
# 3.14159

dm = datetime(2021, 2, 10, 13, 50, 21)
print(format(dm, '%Y-%m-%d %H:%M:%S'))
# 2021-02-10 13:50:21
