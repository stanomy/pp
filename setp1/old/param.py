# -*- coding: utf-8 -*-

#参数

#默认参数
def aa(x,y,z=1):
	return x*y*z

print('调用默认参数1:%d' % aa(3,2))
print('调用默认参数2:%d' % aa(3,2,3))
#可变参数
def bb(*person):
	print('参数长度:%d' % len(person))
	return str(person)

print('调用可变参数0个：%s' % bb())
print('调用可变参数4个：%s' % bb('stanomy',28,'sichuang','CN'))
print('调用可变参数6个：%s' % bb('stanomy',28,'sichuang','CN',22,44))

t=['denghao',33,11,44,'marry']
print('调用list为可变参数t：%s' % bb(t))
print('调用list为可变参数*t：%s' % bb(*t))
#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print('调用关键字参数')
person('ludeng',34,city='zigong')

tt={'school':'Peking','zhuanye':'jsj'}
print('调用关键字参数')
person('lengdong',28,**tt)

def person2(name,age,*,city,job):
	print(name, age, city)

print('调用命名关键字参数')
person2('dengjian',33,city='chengdu',job='tfboy')

#参数组合

def person3(name,age,type,*arg,**kw):
	print('name=',name,'age=',age,'type=',type,'arg=',arg,'kw=',kw)

print('参数组合')
person3('test1',20,2)
person3('test1',20,2,'sichuan','chengdu',job2='jianzhi',job3='job3')