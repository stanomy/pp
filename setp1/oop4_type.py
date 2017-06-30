#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(type(123))
print(type(abs))

import types

print(type(abs)==types.BuiltinFunctionType)

print('isinstance使用')

class A():
	pass

class B(A):
	pass

a=A()
b=B()
print('a is class A',isinstance(a,A))
print('a is class B',isinstance(a,B))
print('b is class A',isinstance(b,A))
print('b is class B',isinstance(b,B))

print('dir()使用')
print(dir('ABC'))

print('hasattr() setattr() getattr() 使用')
print('has attr x',hasattr(a,'x'))
print('set attr x',setattr(a,'x',19))
print('has attr x',hasattr(a,'x'))
print('get attr x',getattr(a,'x'))
