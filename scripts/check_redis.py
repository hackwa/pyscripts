#!/usr/bin/python

# By anurag.d
# Use only if Python-version < 3 
# Refer to this for more info:
# Doc: http://c/display/duSwEnggSysAd/Check_Redis

import argparse,sys,commands,re
import subprocess,time
import telnetlib
#port=6379

# Checks the memory usage of the redis instance

def mem_check(port,host,climit,wlimit):
	memTot=int(commands.getoutput("cat /proc/meminfo | grep MemTotal | awk '{print $2}'"))
	memTot*=1024
	critLimit=climit/100
	warLimit=wlimit/100
	x=commands.getoutput("redis-cli -p %s -h %s info | grep used_memory:"%(port,host))
	curMem=int(x.split()[0].split(":")[1])
	if curMem < warLimit*memTot:
		sys.stdout.write( "Redis %s Memory Status- OK /\
Current memory util:%sK  /"%(port,curMem/1024))
		return 0
	elif curMem > warLimit and curMem < critLimit*memTot:
		sys.stdout.write( "Redis %s Memory Status- Warning (above %s percent) /\
		| Current memory util:%sK  /"%(port,wlimit,curMem/1024))
		return 1
	else:
		sys.stdout.write( "Redis %s Memory Status- Critical (above %s percent) /\
		| Current memory util:%sK  /"%(port,climit,curMem/1024))
		return 2

def check(port,host):
	s=commands.getstatusoutput("redis-cli -p %s -h %s info"%(port,host))[0]
	#print host
	if not s:
		return 0
	else:
		#sys.stdout.write("Could not connect to server ")
		return 1

# Check to see if master-slave link is up or not. Give slave port here

def master_check(port,host):
	
	role=commands.getstatusoutput("redis-cli -p %s -h %s info | grep 'role:' |\
			awk -F : '{print $2}'"%(port,host))[1].split()[0]
	if role == 'slave':
		out=commands.getoutput("redis-cli -p %s -h %s info | grep master_link_status"%(port,host))
		try:
			status=out.split()[0].split(":")[1]
		except:
			sys.stdout.write( "Error! Unable to check replication /")
			return 1
		if status=='up':
			sys.stdout.write( "Master link up /")
			return 0
		elif status=='down':
			out=commands.getoutput("redis-cli -p %s -h %s info | grep master_link_down"%(port,host))
			seconds=out.split()[0].split(":")[1]
			sys.stdout.write( "Master link down since %s seconds /"%seconds)
			return 2
		else:
			print "Unable to check master link /"
			return 1
	elif role == 'master':
		sys.stdout.write("This is a master  /")
		return 0
	


def latency_check(port,host):
	command="redis-cli --latency -p %s -h %s"%(port,host)
	args=command.split(" ")
	#print args
	try:
		p=subprocess.Popen(args,stdout=subprocess.PIPE)
	except:
		None
		sys.exit(2)
	time.sleep(1)
	try:
		p.kill()
	except:
		pid=p.pid
		temp=commands.getoutput('kill -9 %s'%pid)
		if temp:
			print "Error!"
			sys.exit(2)
	out=p.stdout.read()
	latency=re.findall('avg: [0-9].[0-9]+',out)[-1].split(" ")[1]
	sys.stdout.write( "Average latency: %sms /"%latency)
	if float(latency) > 1000:
		sys.stdout.write("Latency Warning!! /")
		return 1
	else:
		return 0

# Check if the server is reachabe via telnet. Retry 3 times

def tcp_reach(port,host):
	for i in range(3):
		try:
			tn = telnetlib.Telnet(host,port)
			tn.write("*1\r\n$4\r\ninfo\r\n")
			x=tn.read_until("used_cpu",3)
			role=re.findall('role:(master|slave)',x)[0]
			if role =='master':
				tn.write("*3\r\n$3\r\nSET\r\n$11\r\na_randomkey\r\n$5\r\nvalue\r\n")
				tn.write("*2\r\n$3\r\nGET\r\n$11\r\na_randomkey\r\n")
				tmp= tn.read_until('value',3).split()
				tn.write("*2\r\n$3\r\nDEL\r\n$11\r\na_randomkey\r\n")
				tn.close()
			        break
			elif role == 'slave':
				tmp=['value']
				break
			else:
				continue
		except:
			if i==2:
				sys.stdout.write("Server %s not Reachable   /"%(port))
				return 2
			else:
				continue
	if tmp[-1] == 'value' :
		sys.stdout.write("Redis %s at %s --OK   /"%(port,host))
		return 0
	else:
		sys.stdout.write('Server %s not Reachable   /'%(port))
		return 2


		 

# What Nonsense is this!

def main():
	parser=argparse.ArgumentParser(description="Arguments Description:")
	parser.add_argument('-p','--port',type=int,required=True,nargs='+',\
			help='Port(s) at which server is running' )
	parser.add_argument('-a','--host',nargs='*',help='Redis host(s) address (default=127.0.0.1)')
	parser.add_argument('-m','--memory',type=float,nargs=2,metavar=('CritLimit',' WarLimit'),\
			help='Checks if the memory usage is within specified percentages')
	parser.add_argument('-l','--latency',const=1,metavar='',action='store_const',\
			help='Latency of the server in milliseconds')
	parser.add_argument('-s','--slave',metavar='',action='store_const',const=1,\
			help='Check if Master-Slave link is up or not')
	parser.add_argument('-r','--reach',metavar='',const=1,action='store_const',\
			help='Check if the server can be reached via tcp.\
			 (Uses telnet)')
	args=parser.parse_args()
	status=run_check(args.port,args.memory,args.latency,args.slave,\
			args.host,args.reach)
	return status

def run_check(p,m,l,s,h,r):
	if h is None:
		h=['127.0.0.1']
	hosts=len(h)
	servers=len(p)
	status=[]
	# check every port for each of the hosts
	for j in range(hosts):
		sys.stdout.write("....Checks for %s......."%(h[j]))
		for i in range(servers):
		#skip this check if tcp check is enabled
			if r is None:
				curCheck=check(p[i],h[j])
				status.append(curCheck)
				if curCheck is 0:
					sys.stdout.write( "\t->%s running / "%(p[i]))
				else:
					sys.stdout.write("\t->%s not accessible / "%(p[i]))
					continue
			else:
				curCheck=tcp_reach(p[i],h[j])
				status.append(curCheck)
				if curCheck is not 0:
					continue
 			if l is not None:
 				status.append(latency_check(p[i],h[j]))
 			if s is not None:
 				status.append(master_check(p[i],h[j])) 	
  			if m is not None: 
 				status.append(mem_check(p[i],h[j],m[0],m[1]))
	return max(status)
if __name__=='__main__':
	r=main()
	sys.exit(r)
