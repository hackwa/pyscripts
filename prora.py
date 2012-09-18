#!/usr/bin/python
#still to add error handling capability

import os
import subprocess
from thread import *
import time
#from socket import *


inpath="/root/input"
opath="/root/output"
repath="/root/result"
ppath="/root/test.cpp"


def mainwa():
	execwa()
	f=open(repath,'r')
	for data in f:
		print data,
	f.close()
	flag=checkwa()
	if flag==0:
		print 'ac'
	else:
		print 'err'
	

def execwa():
	x=subprocess.Popen(('/usr/bin/time','-f \"%E\"','g++',ppath),stderr=subprocess.PIPE).stderr
	twa= x.readline()
	print type(twa)
	twa=twa[4:9]
	print twa
	#compile file
	temp=[]
	inhandle=subprocess.Popen(('cat',inpath),stdout=subprocess.PIPE).stdout
	# input data
	#testhandle=Popen(('cat',opath),stdout=PIPE).stdout
	# test case output
	x=open(repath,'w')
	#time.sleep(1)
	#for data in inhandle:
	
	#	temp.append(data)
	run='/root/a.out'
	h=subprocess.Popen((run ),stdin=subprocess.PIPE,stdout=subprocess.PIPE)
	
	for data in inhandle:
		h.stdin.write(data)
	for data in h.stdout:
		#print data,
		x.write(data)
		#for op in exechandle:
	inhandle.close()

def checkwa():
	r=open(repath,'r')
	o=open(opath,'r')
	for data in o:
		if data != r.readline():
			return 1
		else:
			continue
	return 0;


if __name__=='__main__':
	mainwa()




