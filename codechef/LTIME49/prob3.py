t=input()
while t>0:
	t-=1
	temp={}
	n,x=map(int,raw_input().split())
	P=map(int,raw_input().split())
	C=map(int,raw_input().split())
	K=map(int,raw_input().split())
	child={}
	cost=[0]*n
	for i in range(n):
		child[i]=[]
		temp[i]=[]
	for i in range(n-1):
		child[P[i]].append(i+1)
	for i in range(n):
		temp[i].append(i)
	groups=[]
	t=0
	r=0
	print K
	for i in range(1):
		stack=[]
		stack.append(i)
		visited=[False]*n
		visited[i]=True
		z=K[i]
		r=0
		count=0
		dfs=[]
		while len(stack)>0:
			s=stack.pop()
			dfs.append(s)
			if len(child[s])==0:
				level=K[i]
				l=1
				r=level-1
				print dfs
				for y in range(len(dfs)):
					while l<len(dfs):
						if K[dfs[l]]==r:
							count+=1
							r-=1
						l+=1
					if r<=0:
						cost[i]+=1
				dfs=[i]

			for w in child[s]:
				if visited[w]==False:
					stack.append(w)
					visited[w]=True
	print cost				

