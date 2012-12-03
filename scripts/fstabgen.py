#!/usr/bin/python

# I am not responsible if this file screws up your fstab :P
# Must be run as root

import commands
import re
import os



def mkpath(uid,stat,fstab,typ):
 print 'default path is current dir..'
 for i in range(0,len(uid)):
	if uid[i] not in fstab:
		print 'Enter mount point for following partition...(s to skip)'
		print stat[i]
		mp=raw_input()
		if mp=='s': continue
		while 1:
			try:
				if os.path.exists(mp):break
				os.mkdir(mp)
				break
			except :
				print 'Please try entring path again...'
				mp=raw_input()
		if typ[i]=='swap':
			opt='sw'
		else:
			opt='defaults'
		entry=uid[i]+' '+os.path.abspath(mp)+' '
		entry=entry+typ[i]+' '+opt+' 0 0  \n'
		#print 'fstab entry----->'
		#print entry
		f=open('/etc/fstab','a')
		f.write(entry)
		f.close()

def mainw():
	print 'creating a backup of current fstab as /etc/fstab.old'	
	commands.getstatusoutput('cp /etc/fstab /etc/fstab.old')
	stat=commands.getoutput('blkid')
	uid=re.findall(r'UUID=[A-Za-z"0-9-]+',stat)
	# remove "" from uid
	for i in range(0,len(uid)):
		uid[i]='UUID='+uid[i].split('"')[1]
		#print uid[i]
	# detect types
	typ=re.findall(r'TYPE=[A-Za-z"0-9]+',stat)
	for i in range(0,len(typ)):
		typ[i]=typ[i].split('"')[1]
		#print typ[i]
	# read fstab
	fstab=commands.getoutput(r"awk < /etc/fstab '{print $1}'")
	fstab=fstab.split('\n')
	stat=stat.split("\n")
	# create mount points
	mkpath(uid,stat,fstab,typ)
	print 'generation complete...run "mount -a" to verify'

if __name__=='__main__':
	mainw()
