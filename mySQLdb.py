#!/usr/bin/python

import sys
import MySQLdb as mdb

con=mdb.connect('localhost','root','1','mysql')

def loginw():
	con=mdb.connect('localhost','root','1','mysql')
	print con
	while True :
		uname=raw_input('username : ')
		passwd=raw_input('password : ')
		cur=con.cursor()
		#print cur
		uwa=cur.execute("SELECT *  FROM tablewa WHERE username= '%s'"%(uname))
		pwa=cur.execute("SELECT * FROM tablewa WHERE password= '%s'"%(passwd))
		if uwa==0L:
			print "Username Doesn't Exist Try Again......"
		elif pwa==0L:
			print "Wrong Password Try Again......."
		else:
			print "Login Successful!!"
			print cur.fetchone()[2]
			cur.close()
			con.close()
			return



def registerw():
	con=mdb.connect('localhost','root','1','mysql')
	print con
	while True :
		uname=raw_input('New username : ')
		passwd=raw_input('Password : ')
		descr=raw_input('Description : ')
		cur=con.cursor()
		#print cur
		uwa=cur.execute("SELECT * FROM tablewa WHERE username= '%s'"%(uname))
		if uwa==0L:
			cur.execute("INSERT INTO tablewa VALUES('%s','%s','%s')"%(uname,passwd,descr))
			con.commit()
			cur.close()
			con.close()
			return
		else:
			print "username exists Try again"



def menuw():
	while True:
		print "\n#*******Menu**********#\n"
		print " (l)ogin"
		print " (r)egister"
		#print " (a)dminister databse"
		print " (e)xit"
		ch=(raw_input("Enter your choice : "))
		if ch.lower()=='l':
			loginw()
		elif ch.lower()=='r':
			registerw()
		elif ch.lower()=='e':
			break
		else:
			print "Invalid Option please try again...."


#def adminwa():


if __name__=='__main__':
	menuw()
