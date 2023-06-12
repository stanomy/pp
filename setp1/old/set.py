# -*- coding: utf-8 -*-

s=set([55,66,77,'44'])
print(s)
s=set([55,55,55,'44'])
print(s)
s.add(444)
print(s)
s.remove('44')
print(s)

s1=set([55,44])
print(s & s1)
print(s | s1)