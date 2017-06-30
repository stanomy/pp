# -*- coding: utf-8 -*-

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n)	#123
print(f)	#456.789
print(s1)	#Hello,world
print(s2)	#Hello,'Adam'
print(s3)	#Hello, "Bart"
print(s4)	#

#格式化输出
print('rs:%d' % 3) 

#格式化test
s1=72
s2=85
r=(s2-s1)/s1*100
print('%.1f%%' % r)

#按索引取值
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
#apple
print(L[0][0])
#python
print(L[1][1])
#List
print(L[-1][-1])