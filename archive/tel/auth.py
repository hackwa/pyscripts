#!/usr/bin/python

import re
import os
from commands import getstatusoutput

def check(uname,passw):
	f=open('pass','w')
	f.write(passw)
	f.close()
	x=getstatusoutput('grep \^%s /etc/shadow'%uname)
	if  x[0]: return 'error'
	actual=x[1].split(':')
	actual=actual[1]
	print 'actual->',actual
	salt=x[1].split('$')[2]
	print 'salt->',salt
	hashw=getstatusoutput('mkpasswd -m sha-512 --salt=%s -s < pass'%salt)
	hashw=hashw[1]
	print 'calculated->',hashw
	if hashw == actual:
		return 'Success'
	else:
		return 'No Match'

def main():
	while True:
		uname=raw_input('Username: ')
		passw=raw_input('Password: ')
		status=check(uname,passw)
		print status

if __name__=='__main__':
	main()
