#!/usr/bin/python

import sys
import os
import socket

if len(sys.argv)>1:
	HOST=sys.argv[1]
else:
	HOST=""


for i in range(1,65536):
	tcpSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		tcpSock.connect((HOST,i))
		serv=socket.getservbyport(i)
		print i,'->',serv
		tcpSock.close()
	except:
		None
