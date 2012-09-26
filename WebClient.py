#!/usr/bin/python
# Unfinished

from socket import *

HOST='172.16.32.222'
PORT=80
BUFSIZ=1024
ADDR=(HOST,PORT)

webSock=socket(AF_INET,SOCK_STREAM)
webSock.connect(ADDR)

data=['GET /nab HTTP/1.1',
'Host: 192.168.108.108:8080',
'Connection: keep-alive',
'Cache-Control: max-age=0',
'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.57 Safari/537.1',
'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Encoding: gzip,deflate,sdch',
'Accept-Language: en-US,en;q=0.8',
'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3']


for i in range(len(data)):
	webSock.send(data[i])
while True:
	data=webSock.recv(BUFSIZ)
	print data
webSock.close()



