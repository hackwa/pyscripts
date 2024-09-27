#!/usr/bin/python

# A test server which returns with timestamp whatever data is sent to it

from socket import *
from time import ctime

HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSrk=socket(AF_INET,SOCK_STREAM)
tcpSrk.bind(ADDR)
tcpSrk.listen(5)

while True:
	print 'waiting for connection..'
	tcpClik,addr=tcpSrk.accept()
	print '....connected from :',addr

	while True:
		
                data=tcpClik.recv(BUFSIZ)
	        if not data:
		       break
	        tcpClik.send('[%s] %s' %(ctime(),data))
	tcpClik.close()
tcpSrk.close()
	

