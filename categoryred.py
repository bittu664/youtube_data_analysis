#!/usr/bin/python2
from sys import stdin
count=0
genre={}
for line in stdin:
	y=line.split('\n')
	if y[0] not in genre:
		genre.update({y[0]:1})
	else:
		genre[y[0]]+=1
for i in genre.keys():
	print i+'\t'+str(genre[i])
