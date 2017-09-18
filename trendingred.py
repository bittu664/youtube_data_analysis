#!/usr/bin/python2
import sys
vid={}
view=[]
for ip in sys.stdin:
	y=ip.split('\n')
	x=y[0].split('\t')	
	if x[0] not in vid:
		vid.update({x[0]:int(x[1])})
	view.append(int(x[1]))
view.sort(reverse=1)
for i in range(10):

	for ch in vid.keys():	
		if view[i]==vid[ch]:
			print ch+'\t'+str(vid[ch])
