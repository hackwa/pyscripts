#!/usr/bin/python

# converts base-32 encoding to base-64

# base 32  dictionary
x_32={}
for i in range(32):
	if i<26:
		x_32[i]=chr(65+i)
	else:
		x_32[i]=str(i-24)
#print x_32

# base 64 dictionary
x_64={}
for i in range(62):
	if i<26:
		x_64[i]=chr(65+i)
	elif i<52:
		x_64[i]=chr(71+i)
	else:
		x_64[i]=str(i-52)
x_64[62]='+'
x_64[63]='/'

#print x_64

# 32 base to binary stream
def binwa(ip):
	#print ip
	
	x=''
	if ip.count('=')==4:
		lenwa=16
	elif ip.count('='):
		lenwa=24
	elif ip.count('=')==1:
		lenwa=32
	elif ip.count('=')==6:
		lenwa=8
	else:
		lenwa=40
	for i in range(len(ip)-ip.count('=')):
		#print i
		for j in range(32):
			if x_32[j]==ip[i].upper():
				key=j
				break
		tmp=(bin(int(key)))
		tmp=tmp[2:]
		tmp='0'*(5-len(tmp))+tmp
		#print tmp
		x=x+tmp
	return x[:lenwa]
	
		
# binary stream to 64 base
def base64(ip):
	x=''
	if len(ip)%24==16:
		ip=ip+'00'
		lenwa=18
		pad='='
	elif len(ip)%24==8:
		ip=ip+'0000'
		lenwa=12
		pad='=='
	else:
		lenwa=24
		pad=''
	for i in range(0,lenwa,6):
		tmp=ip[i:i+6]
		#print tmp
		for j in range(64):
			if str('0'*(6-len(bin(j)[2:]))+bin(j)[2:])==tmp:
		        	x=x+str(x_64[j])
		        	break
		#print x
	return x+ pad
		
			



def mainwa():
	for i in range(100):

		ip=raw_input('test case : ')
		binw=''
		for j in range(0,len(ip)-1,8):
			#print 'j : %d'%(j)
			binw=binw+binwa(str(ip[j:j+8]))
			
		
	 	#print binw
		ans=''
		for j in range(0,len(binw)-1,24):
			ans=ans+base64(binw[j:j+24])
		print ans


if __name__=='__main__':
	mainwa()


