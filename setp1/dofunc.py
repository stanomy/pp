from func import a
from func import acheck

#多个返回值
def move(x,y):
	return x+1,y+1

xx,yy=move(10,20)
print(xx,yy)

print(a(-10))
print(acheck('123'))