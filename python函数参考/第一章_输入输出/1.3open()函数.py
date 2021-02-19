# open(file),其中file表示需要打开文件的相对路径
# Demo 1
with open('text.txt', 'r+') as f:  # 以只读方式打开文件
    print('第一次打开文件指针位置', f.tell())
    print('读取一行数据', )
    print(f.readline(), '读取完毕！')
    print('读取完毕后，指针位置！', f.tell())
    # f.seek(0)   # 如果不讲指针调至0   曾曾曾曾曾 将会覆盖 床前明月光
    # f.seek(19)   # 如果不讲指针调至0   曾曾曾曾曾 将会覆盖 疑是地上霜
    print('准备写入数据！', end='')  # 如果不加f.seek() 则 曾曾曾曾曾 会被添加到最后
    f.write('曾曾曾曾曾')
    print('数据写入完成！')
    print('写入完毕后，指针位置！', f.tell())
    print('将指针调制0，输出所有文件')
    f.seek(0)
    print(f.read().encode('utf-8'))

# Demo 2
with open('text.txt', 'r+') as f:
    f.write("喂喂喂喂喂")  # 会从头开始覆盖
    print(f.tell())

# Demo 3
# encode(‘raw_unicode_escape’)方法将类似bytes形式的字符串转换成bytes
s = '\xe7\xbb\x9d\xe5\x9c\xb0\xe6\xb1\x82\xe7\x94\x9f'
ss = s.encode('raw_unicode_escape')
print(ss)  # b'\xe7\xbb\x9d\xe5\x9c\xb0\xe6\xb1\x82\xe7\x94\x9f'
print(ss.decode())

# decode(‘raw_unicode_escape’)方法输出内容为bytes形式的字符串
# print(type(ss))
d = '绝地求生'
dd = d.encode()
print(dd)
print(dd.decode('raw_unicode_escape'))

# read([size])
with open('text.txt', 'r') as f:
    f.read(10)  # 10个字符   所有字符均按一个计算，包括汉字，如“name：无”的字符数为6

# readline([size])
with open('text.txt', 'r') as f:
    f.readline(10)  # 10个字符  读取一行中的前10 个字符,如果该行没有10个字符，就读取整行

# readlines()
with open('text.txt', 'r') as f:
    f.readlines()  # 返回行组成的列表

# write(obj)
# tell()  返回当前文件指针的位置，二进制模式下距离文件头的字节数
# 使用tell()方法返回的位置与为read()方法指定的size参数不同。tell()方法返回的不是字符的个数，
# 而是字节数，其中汉字所占的字节数根据其采用的编码有所不同，如果采用GBK编码，则一个汉字按两个字符计算；如果采用UTF-8编码，则一个汉字按3个字符计算。
# seek(offset,[whence]) offset移动的字节个数，whence表示 位置  开头、当前、结尾
# close()

# Demo 4
for line in open('./text.txt', 'r'):
    print(line.strip().strip('\n').strip('\t'))

# 多文件读取操作
