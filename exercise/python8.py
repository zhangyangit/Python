#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

l = [1, 2, 3, 4 ,5]
for i in range(len(l)):
	print l[i]
	time.sleep(10)

myID = {1:'zhang', 2:'yan'}
for key, value in dict.items(myID):
	print key, value
	time.sleep(10)



