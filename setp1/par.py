# -*- coding: utf-8 -*-

print('偏函数，类似类型转换')

def change(type,*arg):
	return int(*arg,type)

print(change(10,"123"))


import functools

int2=functools.partial(int,base=10)
print(int2("3333"))