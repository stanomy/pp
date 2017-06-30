#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a module test'

__author__='sy'

import sys

def test():
	args=sys.argv
	if len(args)==1:
		print('Hello world')
	elif len(args)==2:
		print('Hello %s' % args[1])
	else:
		print('Too many arguments')
	
	

if __name__=='__main__':
	test()
	
print('name=%s' % __name__)
print('作用域test')

def _private_1(name):
	return 'hello %s' % name

def _private_2(name):
	return 'Hi %s' % name

def greeting(name):
	if len(name) >3:
		return _private_1(name)
	else :
		return _private_2(name)


print(greeting('thr'))
print(greeting('four'))