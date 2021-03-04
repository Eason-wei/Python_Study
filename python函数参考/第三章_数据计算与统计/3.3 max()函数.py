# max()获取可迭代对象（或元素）的最大值
list = ['e','d',"曾"]
print(max(list))
fun1 = lambda x,y:x+y
print(fun1(1,2))

dictall={'大众':643518,'奔驰':319163,'宝马':265051,'福特':252323,'雪铁龙':227967,'雷诺':130825,'现代':114878,'奥迪':255300}
list_value = dictall.values()
list_keys = dictall.keys()
print(list_value)
print(list_keys)
zipped = zip(list_value,list_keys)
print(max(zipped,key=lambda x:x[1]))