#! /usr/bin/python

# A custom simple telnet client for my telnet server

import socket
import thread
import sys

HOST='127.0.0.1'
PORT=42
BUFSIZ=1024

tcpClik=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def threadw(tcpClik):
	while True:
		rcv=tcpClik.recv(BUFSIZ)
		print rcv,
	
def mainw():	
	print 'starting client...'
	print 'enter "exit" to quit...'
	HOST=raw_input("Open->")
	ADDR=(HOST,PORT)
	try :
		tcpClik.connect(ADDR)
	except socket.error, e : 
		print 'Error in connection..',e
		sys.exit()
	thread.start_new_thread(threadw,(tcpClik,))
	while True:
		data=raw_input()
		if data=='exit':
			break
		try:
			tcpClik.send(data)
		except socket.error,e:
			print 'connection with remote server broke'
			sys.exit()
	print 'exiting..'
	tcpClik.close()

if __name__=='__main__':
	mainw()
