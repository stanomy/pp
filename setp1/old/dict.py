# -*- coding: utf-8 -*-

t={'1':1,'sm':'sm','teest':3}
print('t='+str(t))
print('从dict t中去key为1的value='+str(t.get('1')))
#不存在则返回指定值
print(t.get('ac'),'ac')
print('teest' in t)
t['abc']='abcv'
print(t['abc'])
print(t.pop('abc'))
print('abc' in t)