#!/usr/bin/python
# A basic web server with html and php capabilities
# Can handle only 200 and 404

from socket import *
from time import ctime
fopen = open
from os import *
from thread import *
from subprocess import *
import re

docRoot='/www'
HOST=''
PORT=8080
BUFSIZ=1024
ADDR=(HOST,PORT)
TYPE='html'

# a general response

response=['HTTP/1.1 200 OK',
		'Date: Mon, 23 May 2005 22:38:34 GMT',
		'Server: NAB/1.3.3.7 (Unix) (Ubuntu/Linux)',
		'Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT',
		'Etag: "3f80f-1b6-3e1cb03b"',
		'Accept-Ranges:  none',
		'Content-Length: 43',
		'Connection: close',
		'Content-Type: text/html; charset=UTF-8','\n\n']

webSock=socket(AF_INET,SOCK_STREAM)
webSock.bind(ADDR)
webSock.listen(3)
rcv=[]

# main function
def nab():
       while True:
	        print 'waiting for connection...'
	        webClik,addr=webSock.accept()
	        print '...connected from : ',addr
		rcv=[]
		start_new_thread(receiwe,(webClik,))
	
       webSock.close()



#thread to handle requests
def receiwe(socketwa):

        data=socketwa.recv(BUFSIZ)
        rcv=[data]
        print data
	
	TYPE='html'

	pathwa=rcv[0].split(" ")
	path=pathwa[1]
	#extract the relative path from request
	#print path
	if path=='/':
		path=docRoot+'/index.html'
	elif re.findall('(\.php)$',path)==['.php']:
		path=docRoot+path
	        TYPE='php'
	else:

		path=docRoot+path+'.html'
	print path
	try:
	        fobj=fopen(str(path),'r')
	except IOError,e:
		#if file doesn't exist then give 404 response
		
		print 'error hua hai!!!!!!!!!!!!!!!!'
		error=('HTTP/1.1 404 NOT FOUND','\n\n')
		for i in range(len(error)):
		     socketwa.send(error[i])
		fobj=fopen('/www/error.html','r')
		for i in fobj:
			socketwa.send(i)
		fobj.close()
		socketwa.close()
		return
	
	# html request
	if TYPE=='html':
		print 'in htmlwaa................'
                for i in range(len(response)):
		        socketwa.send(response[i])
		print 'sending datawa..........'
		for i in fobj:
			socketwa.send(i)
		fobj.close()
		recv=[]
		socketwa.close()
	#php request
	else:
		print 'in PHP...................'
		f=Popen(('php','-f',path),stdout=PIPE).stdout
		for i in range(len(response)):
			socketwa.send(response[i])
		for data in f:
			socketwa.send(data)
		socketwa.send('nab\n')
		f.close()
		fobj.close()
		recv=[]
		socketwa.close()
		
		


	
if __name__=='__main__':
	
	try:
		nab()
	except:
		webSock.close()
