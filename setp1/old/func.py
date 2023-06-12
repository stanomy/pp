# -*- coding: utf-8 -*-
#函数别名
def a(b):
	return abs(b)
	
def acheck(b):
	if not isinstance(b,int):
		raise TypeError('参数类型不对')
	return abs(b)

