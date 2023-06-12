# -*- coding: utf-8 -*-
from collections import Iterable
#test是否迭代器
print('isinstance([],Iterable):'+str(isinstance([],Iterable)))
print('isinstance({},Iterable):'+str(isinstance({},Iterable)))
print('isinstance(set(),Iterable):'+str(isinstance(set(),Iterable)))


it=iter(range(5))

for x in it:
	print(x)