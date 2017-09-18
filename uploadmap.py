#!/usr/bin/python2
from sys import stdin
for line in stdin:
	l=line.split('\t')
	if len(l)>=3: 
		print l[1]
