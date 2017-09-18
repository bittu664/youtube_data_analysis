#!/usr/bin/python2
from sys import stdin
count=0
upload={}
for line in stdin:
	y=line.split('\n')
	if y[0] not in upload:
		upload.update({y[0]:1})
	else:
		upload[y[0]]+=1
count=[]
for itm in upload.keys():
	count.append(upload[itm])
count.sort(reverse=1)
num=0
for i in range(10):
	for itm in upload.keys():
		if upload[itm]==count[i]:
			print itm+' '+str(upload[itm])
			upload[itm]=-1			
			num+=1
			if num==10:
				break			
	if num==10:
		break




