#!/usr/bin/python

# BASH shell with some custom as well as native commands 
# To fix-History support

import os
from commands import getstatusoutput
import random
import subprocess



print ('Enter "help" to see the list of commands')


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
			print 'Command does not Exist'
			
	
def custw():
	while 1 :
		cmd=raw_input("Shellwa:~# ")
		if cmd=='exit':return
		if cmd=='':None
		else:
			s,x=getstatusoutput((cmd))
			if s:
				print "attempt to execute unsuccessful.."
			else:
				#for y in x:
				print x


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
