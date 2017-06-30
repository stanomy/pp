# -*- coding: utf-8 -*-
#排序
t=[4,-2,5,1,-133,2,3,2]
print(sorted(t))

#key
print(sorted(t,key=abs))

#job 对名字进行排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return t[0]
	
print(sorted(L))
		