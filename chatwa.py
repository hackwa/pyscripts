#!/usr/bin/python
# a basic LAN chat app


from socket import *
from time import ctime
from thread import *

SPORT=int(raw_input('Run Chat Server at Port : '))
CPORT=int(raw_input('Connect to other Server at Port S:'))
SHOST=''
CHOST='127.0.0.1'
BUFSIZ=1024
SADDR=(SHOST,SPORT)
CADDR=(CHOST,CPORT)

def Serverwa():
	tcpSrk=socket(AF_INET,SOCK_STREAM)
	tcpSrk.bind(SADDR)
	tcpSrk.listen(3)

	while True:
		print 'waiting for connection...'
		tcpClik,addr=tcpSrk.accept()
		print '...connected from : ',addr

		while True:
			data=tcpClik.recv(BUFSIZ)
			if not data:
				break
			print ('[%s] %s' %(ctime(),data))
		tcpClik.close()
	tcpSrk.close()

def Clientwa():
	tcpClik=socket(AF_INET,SOCK_STREAM)
	tcpClik.connect(CADDR)

	while True:
		data=raw_input('> ')
		if not data:
			break
		tcpClik.send(data)
	tcpClik.close()

def nab():
	print 'Starting local Server..'
	start_new_thread(Serverwa,() )
	print 'enter y to start Client..'
	while True:
		inwa=raw_input('')
		if inwa=='y':
			break

	Clientwa()

if __name__=='__main__':
	nab()
