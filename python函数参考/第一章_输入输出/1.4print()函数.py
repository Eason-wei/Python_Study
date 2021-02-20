# print(value,sep,end,file=sys.stdout,flush=False)
print('go', 'big', 'or', 'go', 'home', sep='---')  # sep 是连接符
print('输出到同一行', end=' ')
# 使用三引号可多行输出字符，如三行输出的服务器登录界面
print('''
    登录服务器
    管理员：_______________
    密码：____________
''')
print(chr(8544), chr(8545), chr(8546), chr(8547))  # 输出：Ⅰ Ⅱ Ⅲ Ⅳ
print(ord('生'), ord('化'), ord('危'), ord('机'))  # 输出：29983 21270 21361 26426

name = ['杨过', '临安', '1224', '小龙女']
print('--'.join(name))
print(' '.join(name))
print(''.join(name))

instr = input("请输入一个数字")
print(instr.zfill(5))  # 输出5位数字编号
print('nHex = %x,nDec = %d,nOct = %o' % (123, 123, 123))

# Demo 1 对齐数据
team = '格陵兰岛'
print(team.ljust(10, "*"))  # 靠左对齐，占位10个字符，不足的用*表示
print(team.rjust(10, '-'))  # 靠右对齐，占位10字符，不足用-表示

# Demo 2 输出到文件
fp = open('text.txt', 'a+')
str_e = 'hello , Python'
print(str_e, file=fp)
fp.close()

# Demo 动态刷新控制台输出
import time

for i in range(10, -1, -1):
    time.sleep(1)
    print('\n距离结束还有{0:0>3}'.format(i), 'S', end='')
    print('\r距离结束还有{0:0>3}'.format(i), 'S', end='')

from reprint import output
import time
import random

with output(initial_len=3, interval=0) as output_lines:
    while True:
        rate_line_0 = random.randint(10, 99)
        # print(rate_line_0)
        rate_line_1 = random.randint(10, 99)
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        output_lines[0] = '| 177777 | Python + 树莓派从入门到实践 | {}% | 2020-05-20 10:24:48 |'.format(rate_line_0)
        output_lines[1] = '+--------+------------------------------+------------+---------------------+'
        output_lines[2] = '| 188446 | Python + Kivy（App开发） 从入门到实践 | {}% | {}% |'.format(rate_line_1, now_time)
        time.sleep(1)
