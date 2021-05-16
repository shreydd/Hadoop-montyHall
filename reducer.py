#!/usr/bin/env python3

from operator import itemgetter
import sys

sumprob = 0

for line in sys.stdin:
	res = line.strip('[]')
	res = res.strip(']\t\n')
	res = res.split(', ')
	for r in res:
		sumprob += float(r)
	print(sumprob/3)
