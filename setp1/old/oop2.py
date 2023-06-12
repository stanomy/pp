#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class teacher():
	def __init__(self,name,address):
		self.__name=name
		self.address=address


tWang=teacher('wang','sichuang')
print('访问公共属性')
print(tWang.address)
print('访问内部属性1')
print(tWang._teacher__name)
print('访问内部属性2')
print(tWang.__name)
