# -*- coding: utf-8 -*-

#函数作为返回值测试
def sum(*x):
	
	def sum1():
		ss=0
		for y in x:
			ss=ss+y;
		return ss
	return sum1

f=sum(1,2,3)

print(f)
print(f())
print(sum(5))


#闭包函数
def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

		
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())

#闭包2
def count1():
	def f(j):
		def g():
			return j*j;
		return g
	fs=[]
	for i in range(1,4):
		fs.append(f(i))
	return fs

f3,f4,f5=count1()
print(f3())
print(f4())
print(f5())
