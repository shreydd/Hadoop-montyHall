#!/usr/bin/env python3
from operator import itemgetter
import sys

sumprob = 0
i = 0
for line in sys.stdin:
	sumprob += float(line)
	i+=1
print(sumprob/i)