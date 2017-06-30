# -*- coding: utf-8 -*-

#声明一个生成器
g=(x*x for x in range(20))

#生成器的next,打印g的值
y=0
while y<10:
	print(next(g))
	y=y+1

#生成器函数
z=0
def obb():
	return z+1
	yield
	

for i in obb():
	print(i)
	

def triangles():
	yield