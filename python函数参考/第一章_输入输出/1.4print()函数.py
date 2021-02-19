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
