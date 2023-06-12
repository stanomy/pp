# -*- coding: utf-8 -*-
L = ['Hello', 'World', 18, 'Apple', None]

print([str(s).lower() for s in L])
print([s.lower() for s in L if isinstance(s,str)])