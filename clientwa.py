#! /usr/bin/python

from socket import *

HOST='127.0.0.1'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpClik=socket(AF_INET,SOCK_STREAM)
tcpClik.connect(ADDR)

while True:
	data=raw_input('> ')
	if not data:
		break
	tcpClik.send(data)
	data=tcpClik.recv(BUFSIZ)
	if not data:
		break
	print data

tcpClik.close()
