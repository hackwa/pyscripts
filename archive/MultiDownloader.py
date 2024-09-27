#!/usr/bin/python

# A basic download manager to download a given url using 4 threads
# Still to add exception handling 

import os
import urllib
import urllib2
import sys
import thread 
import threading
from urlparse import urlparse

# overload init of original Thread class

class myThread(threading.Thread):
	def __init__(self,a,b,c):
		self.tno=a
		self.chunk=b
		self.urlwa=c
		threading.Thread.__init__(self)
	def run(self):
		threadwa(self.tno,self.chunk,self.urlwa)
		print "Exiting",(self.tno+1),'...','\n'



def threadwa(tno,chunk,urlwa):
	print 'Starting Thread ',tno+1,'...','\n'
	head={}
	stb=tno*chunk
	enb=stb+chunk-1
	if tno==3:
		enb=enb+3
	# remainder
	rangewa='bytes='+str(stb)+'-'+str(enb)
	head['Range']=rangewa
	print head,'\n'
	x=urllib2.Request(urlwa,headers=head)
	try:
		wa=urllib2.urlopen(x)
	except urllib2.HTTPError,err:
		print "Thread Errorwa"
		return 
	f=open("temp%s"%tno,"w")
	f.write(wa.read())
	f.close()
	return 0

	
# Main Function which takes an URL and starts the threads

def mainwa():
	w=x=y=z=1
	urlwa=raw_input("Url To Download : ")
	x=urllib2.Request(urlwa)
	try:
		f=urllib2.urlopen(x)
		meta=f.info()
		size=int(meta.getheaders("Content-Length")[0])
		print "File size : ",size
	# get the size of the file
	except urllib2.HTTPError,errwsad:
		print "HTTP errorwa",errwa.code()
		sys.exit()
	chunk=size/4
	# print chunk
	
	# print "meow"
	# Thread objects
	thread1=myThread(0,chunk,urlwa)
	thread2=myThread(1,chunk,urlwa)
	thread3=myThread(2,chunk,urlwa)
	thread4=myThread(3,chunk,urlwa)

	# start Threads
	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()

	# wait till downloads are complete

	thread1.join()
	thread2.join()
	thread3.join()
	thread4.join()

	print "Download Complete!!"
	print "Appending Individual Part Files"
	x=urlparse(urlwa)
	y=x.path
	y=y.split('/')
	fileName=y.pop()
	f=open(fileName,'w')
	for i in range(4):
		tmp='temp'+str(i)
		temp=open(tmp,'r').read()
		for data in temp:
			f.write(data)
	

	

if __name__=='__main__':
	mainwa()



	






