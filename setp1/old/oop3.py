#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person(object):
	def __init__(self,name,age):
		self.name=name
		self.__age=age
	
	def whoami(self):
		return self.name



class Man(Person):
	
	def howold(self):
		return self.__age

a=Man('li',28)
print('打印继承属性name')
print(a.whoami())
print('打印不能继承属性__age')
print(a.howold())