#!/usr/bin/python

# A telnet server which is made without the use of standard Network Virtual Terminal (NVT)
# protocol. It won't work with standard telnet client. The required client is provided in
# the folder. It cannot work with interactive commands since NVT is not implemented.

import os
from time import ctime
import thread
import subprocess
import commands
from commands import getstatusoutput
import socket
import sys

HOST=''
PORT=42
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpSrk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSrk.bind(ADDR)
tcpSrk.listen(5)

# Returns userid
def uidw(uname):
	x= commands.getoutput(r'cat /etc/passwd | grep %s'%(uname))
	if not x[0]:
		return int(str.split(':')[3])
	else:
		return -1

#uses SHA-512 to verify password
def check(uname,passw):
	f=open('pass','w')
	f.write(passw)
	f.close()
	x=getstatusoutput('grep ^%s /etc/shadow'%uname)
	if x[0] : return 0
	actual=x[1].split(':')
	actual=actual[1]
	print 'actual->',actual
	salt=x[1].split('$')[2]
	print 'salt->',salt
	hashw=getstatusoutput('mkpasswd -m sha-512 --salt=%s -s < pass'%salt)
	hashw=hashw[1]
	print 'calculated->',hashw
	if hashw==actual:
		print 'Matched!'
		return 1
	else:
		return 0

	
def mainw():
	while True:
		print 'waiting for connection..'
		tcpClik,addr=tcpSrk.accept()
		print '...connected from : ', addr
		thread.start_new_thread(threadw,(tcpClik,))
	tcpSrk.close()	
	
# Thread to handle a request
def threadw(tcpClik):
	print 'starting thread'
	while True:
		tcpClik.send('Username: ')
		uname=tcpClik.recv(BUFSIZE)
		print 'uname: ',uname
	
		tcpClik.send('Password: ')
		passwd=tcpClik.recv(BUFSIZE)
		print 'password: ',passwd
		checkw=check(uname,passwd)
		if checkw==1:
			break
		else:
			tcpClik.send('Error!! Please try again...\n')
	uid=uidw(uname)
	os.setreuid(uid,uid)
	tcpClik.send('Logged in successfully..\n')
	tcpClik.send(' * Documentation:  https://help.ubuntu.com/ \n\n')
	host=commands.getoutput('hostname')
	while True:
		try:
			tcpClik.send('\n%s@%s:~$ '%(uname,host))
			data=tcpClik.recv(BUFSIZE)
			cdw=0
			if data.split(" ")[0]=='cd':
				cdw=testForCd(data,uname,tcpClik)
			if cdw ==1:
				continue
			out=commands.getstatusoutput(data)
			print out
			if not out[0]:
				tcpClik.send(out[1])
			else:
				tcpClik.send('Unable to execute')
		except Exception, e:
			print 'Error in thread!!',e
			print 'Closing thread..'
			return

def testForCd(data,uname,tcpClik):
	temp=data.split(" ")
	try:
		if len(temp)==1:
			os.chdir('/home/%s'%uname)
		else:
			dirw=temp[1]
			os.chdir(dirw)
		return 1
	except Exception , e:
		print e
		tcpClik.send('Unable to change dir..\n')
		return 0

if __name__=='__main__':
	mainw()
