# -*- coding: utf-8 -*-
import math


def quadratic(a,b,c):
	if not (isinstance(a,int) or isinstance(b,int) or isinstance(c,int)):
		raise TypeError('参数类型不对')
	x1=2*c/(-b+math.sqrt(b**-4*a*c))
	x2=2*c/(-b-math.sqrt(b**-4*a*c))
	return x1,x2
	
xx,yy=quadratic(2,1,1)
print(xx,yy)