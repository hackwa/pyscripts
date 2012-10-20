#!/usr/bin/python

# Must be run as root for proper function
# BASH shell with some custom as well as native commands 
# To fix-History support

import os
from commands import getstatusoutput
import random
import subprocess
import re
import commands



print ('Enter "help" to see the list of commands')

########### Functions START HERE #############

# Function which provides authentication
def check(uname,passw):
	f=open('/tmp/pass','w')
	f.write(passw)
	f.close()
	x=getstatusoutput('grep ^%s /etc/shadow'%uname)
	if x[0] : return 0
	actual=x[1].split(':')
	actual=actual[1]
	#print 'actual->',actual
	salt=x[1].split('$')[2]
	#print 'salt->',salt
	hashw=getstatusoutput('mkpasswd -m sha-512 --salt=%s -s < pass'%salt)
	hashw=hashw[1]
	#print 'calculated->',hashw
	if hashw==actual:
		print 'Matched!'
		return 1
	else:
		print 'Wrong Password!!'
		return 0

# Returns userid
def uidw(uname):
	x= commands.getstatusoutput(r'cat /etc/passwd | grep %s'%(uname))
	if not x[0]:
		return int(x[1].split(':')[3])
	else:
		return -1

def helpw():
	print '\n *****list of commands*****'
	print ' help'
	print ' pwd'
	print ' ls'
	print ' cd'
	print ' exit'
	print ' cat'
	print ' touch'
	print ' custom'
	print ' kurkure'
	print ' \'h\' for previous command' 

def pwdw():
	pwd = os.getcwd()
	print pwd

def lsw(dirwa=None):
	if dirwa==None:
	         pwd=os.getcwd()
	         ls=os.listdir(pwd)
	 
        else :
		 ls=os.listdir(dirwa)
        for i in ls:
		 print i



def cdw(dirwa=None): 
	if dirwa==None:
		os.chdir('/home/anurag')
	else:
		os.chdir(dirwa)

def catw(filename):
	if filename not in os.listdir(os.getcwd()):
		print 'Errorwa! file does not exist'
		return
	else:
		f=open(os.getcwd()+'/'+filename,'r')
		for eachline in f:
			print eachline,
		f.close()

def touchw(filename):
	f=open(os.getcwd()+'/'+filename,'w')
	f.close()

########### MAIN STARTS HERE #############

def prime():
	
	recent=[]
	history=0
	while True:
	
		
		if not history :		
			cmd1=raw_input('Shellwa:~$ ')
			recent.append(cmd1)
			cmd=cmd1.split(" ")
		else:
			cmd=cur.split()
			#print 'here'
			history=0
			recent.append(cur)
		if cmd[0] =='help':
			helpw()
		elif cmd[0]=='pwd':
			pwdw()
		elif cmd[0]=='ls':
			if len(cmd)>1:
				lsw(cmd[1])
			else:
				lsw()
		elif cmd[0]=='cd':
			if len(cmd)>1:
			        cdw(cmd[1])
			else :
				cdw()
                elif cmd[0]=='cat':
			catw(cmd[1])

		elif cmd[0]=='touch':
			touchw(cmd[1])

		elif cmd[0]=='custom':
			print "Custom shell initiated..(exit to return)"
			custw()
		elif cmd[0]=='kurkure':
			kurkurew()
		elif cmd[0]=='exit':
			break
		elif cmd[0]=='':
			None
		elif cmd[0]=='h':
			if recent[0] is None:break
			else:
				cur=recent.pop()
				cur=recent.pop()
				history=1
				#print 'nab','>>',cur
		else: 
			print 'Command does not Exist (try custom shell)'
			
############ CUSTOM SHELL ##############	

def custw():
	currentUser='root'
	while 1 :
		cmd=raw_input("%s@Shellwa:~# "%currentUser)
		if cmd=='\n': continue
		if cmd=='exit':return
		if cmd=='':continue
		temp=cmd.split(' ')
		if temp[0]=='su':
			if len(temp)==1:
				uname='root'
			else:
				uname=temp[1]
			passwd=raw_input("Password:")
			x=check(uname,passwd)
			if x==0:
				print "Error!! Please Try Again.."
				continue
			else:
				uid=uidw(uname)
				currentUser=uname		
				print uid
				print 'Login is Successful...'
				continue	
		if temp[0] =='cd':
			if len(temp)>1:
			        cdw(temp[1])
			else :
				cdw()
		else:
			s,x=getstatusoutput(('sudo -u %s %s'%(currentUser,cmd)))
			if s:
				print "attempt to execute unsuccessful.."
			else:
				#for y in x:
				print x

######### FUN COMMAND ###########

def kurkurew():
	rand=random.randint(0,9)
	f=open("/root/python/kurkure",'r')
	for x in range(10):
		line=f.readline()
		if x==rand :
			print line,
		else:
			None
	f.close()



if __name__=='__main__':
	prime()
