#!/usr//bin/python
# -*- coding: utf-8 -*-

l = []

for i in range(3):
	x = int(raw_input('interger:\n'))
	l.append(x)
l.sort(reverse=True)
print l
