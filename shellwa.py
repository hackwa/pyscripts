#!/usr/bin/python

import os
from commands import getstatusoutput
import random



print ('Enter "help" to see the list of commands')


def helpwa():
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

def pwdwa():
	pwd = os.getcwd()
	print pwd

def lswa(dirwa=None):
	if dirwa==None:
	         pwd=os.getcwd()
	         ls=os.listdir(pwd)
	 
        else :
		 ls=os.listdir(dirwa)
        for i in ls:
		 print i



def cdwa(dirwa=None): 
	if dirwa==None:
		os.chdir('/home/anurag')
	else:
		os.chdir(dirwa)

def catwa(filename):
	if filename not in os.listdir(os.getcwd()):
		print 'Errorwa! file does not exist'
		return
	else:
		f=open(os.getcwd()+'/'+filename,'r')
		for eachline in f:
			print eachline,
		f.close()

def touchwa(filename):
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
			helpwa()
		elif cmd[0]=='pwd':
			pwdwa()
		elif cmd[0]=='ls':
			if len(cmd)>1:
				lswa(cmd[1])
			else:
				lswa()
		elif cmd[0]=='cd':
			if len(cmd)>1:
			        cdwa(cmd[1])
			else :
				cdwa()
                elif cmd[0]=='cat':
			catwa(cmd[1])

		elif cmd[0]=='touch':
			touchwa(cmd[1])

		elif cmd[0]=='custom':
			print "Custom shell initiated..(exit to return)"
			custwa()
		elif cmd[0]=='kurkure':
			kurkurewa()
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
			
	
def custwa():
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


def kurkurewa():
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
