#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
		
	def print_obj(self):
		print('obj.name=%s obj.score=%d' % (self.name,self.score))
		
print('对象调用')

lisa=Student('lily',98)

lisa.print_obj()

print('内置属性')
print("__dict__",list.__dict__)
print("__doc__",list.__doc__)
print("__name__",list.__name__)
print("__module__",list.__module__)
print("__bases__",list.__bases__)