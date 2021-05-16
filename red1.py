#!/usr/bin/env python3

from operator import itemgetter
import sys

sumprob = 0


for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

word = word.strip('[]')
a,b,c = word.split(',')
sumprob = float(a) + float(b) + float(c)

avg = sumprob/3
print(avg)