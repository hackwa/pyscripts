#!/usr/bin/python

def pro():
	nodes=int(raw_input())
	edges=int(raw_input())
	visited=[]
	ar=[]
	#create empty array
	for i in range(nodes):
		visited.append(0)
		ar.append([])
		for j in range(nodes):
			ar[i].append(0)

	for i in range(edges):
		t1=int(raw_input())
		t2=int(raw_input())
		ar[t1-1][t2-1]=1
	print ar
	q=[]
	#a queue with operations q.insert and q.pop
	cur=0
	print cur+1
	visited[cur]=1
	q.insert(cur,0)
	while len(q):
		cur=q.pop()
		for i in range(nodes):
			if ar[i]:
				if not visited[i]:
					print i+1
					q.insert(i,0)
					visited[i]=1



	





if __name__=='__main__':
	pro()
