# -*- coding: utf-8 -*-

def show_name(x):
	pirnt(x)

f=show_name;

print('函数名%s' % f.__name__)


#装饰器
def log(func):
	def wrapper(*args,**kw):
		print("call %s" % func.__name__)
		return func(*args,**kw)
	return wrapper

#和切面类似,动态修改
@log
def now_time():
	print('2017-0503')

now_time()

#带文本装饰器

def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print("call %s %s()" % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log('show time')
def now():
	print('2017-05-03')

now2=log('show time2')(now)
now()
now2()

#
print('装饰器作业')
def log_job(*arg):
	def dec(func):
		def wrapper(*args,**kw):
			print('begin call')
			if len(arg)>0:
				print("call %s %s()" % (arg[0],func.__name__))
			else:
				print("call %s()" % func.__name__)
			print('end call')
			return func(*args,**kw)
		return wrapper
	return dec

@log_job()
def tt():
	print("first")

@log_job("adv")
def ff():
	print('second')

tt()
ff()
