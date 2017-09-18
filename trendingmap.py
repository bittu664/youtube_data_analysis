#!/usr/bin/python2
import sys
for i in sys.stdin:
	l=i.split('\t')
	if len(l)>=3:
		print l[0]+'\t'+l[5]
