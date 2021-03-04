# abs()获取数字的绝对值
list =['18',12.45,'ASD','明日科技',0,-19.69]
for num in list:
    if isinstance(num,(int,float)):
        print(abs(num))
list1 = [-26,+12,-19,+30,-6,+39]
list2 = sorted(list1,key=abs)
print(list2)

# abs()函数与math.fbs()函数比较
# abs()参数可以是浮点数、整数、复数返回值保持原有数据类型
# math.fbs()返回的总是浮点数

