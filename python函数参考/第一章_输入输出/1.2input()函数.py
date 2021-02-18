score = int(input("请输入整数："))
print("你输入的数字为：",score)

name = input("请输入您的姓名：").strip(' ')     #去除输入两侧的空格 lstrip()  rstrip()
print(name)

x,y = input("请输入两个数字，并且用逗号分开").split(',')
print(x,y)

for x in input("请输入多个数字，中间采用空格分开：").split(' '):
    print(x)

password = input("请输入密码：").upper()
print(password)

n = input("请输入一个字符：")
print(ord(n))    # ord 返回ASCII码

name1 = input("")     #无提示型输入，不换行
name2 = input("请输入姓名：")     #不换行
name3 = input("姓名：\n")      #换行

data_1 = [input("姓名:"),input("年龄:"),input("学校:")]
print(data_1)

a,b = map(int,input("请输入两个数字，用空格分开").split(' '))
print(a,b)