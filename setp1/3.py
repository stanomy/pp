# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5
rule=weight/(height*height)
rule=int(input('请输入体重'))
if rule<18.5:
	print('过轻')
elif rule>=18.5 and rule<=25:
	print('正常')
elif rule>25 and rule<=28:
	print('过重')
elif rule>28 and rule<=32:
	print('肥胖')
elif rule>32:
	print('严重肥胖')