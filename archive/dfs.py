#!/usr/bin/python	

def pro():
	nodes=int(raw_input())
	edges=int(raw_input())
	visited=[]
	ar=[]
	#create an empty array
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
	stack=[]
	#a stack with operations append() and pop()
	cur=0
	stack.append(cur)
	#print cur
	neib=0
	while len(stack):
		neib=0
		for i in range(nodes):
			if ar[i]:
				if not visited[i]:
					neib=1
					break
				else:
					continue
		if neib:
			cur=i
			stack.append(cur)
			print cur+1
			visited[cur]=1
		else:
			cur=stack.pop()


if __name__=='__main__':
	pro()
