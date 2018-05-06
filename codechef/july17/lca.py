import math
def preprocess():
	for i in range(1,n+1):
		j=0
		while (1<<j)<n:
			j+=1
			P[i][j]=-1
	for i in range(2,n+1):
		P[i][0]=parent[i]
	j=1
	while (1<<j)<n:
		for i in range(1,n+1):
			if P[i][j-1]!=-1:
				P[i][j]=P[P[i][j-1]][j-1]
		j+=1
def lca(u,v):
	if level[u]<level[v]:
		temp=v
		v=u
		u=temp
	dist=level[u]-level[v]
	while dist>0:
		raiseby=int(math.log(dist,2))
		u=P[u][raiseby]
		dist-=(1<<raiseby)
	if u==v:
		return u
	for j in range(max_log,-1,-1):
		if (P[u][j]!=-1) and (P[u][j]!=P[v][j]):
			u=P[u][j]
			v=P[v][j]
	if u in parent:
		return parent[u]
	else:
		return parent[v]

max_nodes=100005
max_log=17
P=[[-1 for x in range(max_log+10)] for y in range(max_nodes)]
level=[0]*max_nodes
visited=[0]*max_nodes
gobar=[0]*max_nodes
parent=[1]*max_nodes
t=input()
while t>0:
	t-=1
	n=input()
	graph={}
	for i in range(1,n+1):
		graph[i]=[]
	ma=-1
	for i in range(n-1):
		u,v,c=map(int,raw_input().split())
		ma=max(ma,c)
		graph[u].append([v,c])
		graph[v].append([u,c])
	start=1
	q=[start]
	root=1
	bfs_tree={}
	bfs_tree[start]=0
	for i in range(n+1):
		visited[i]=0
	while q:
		current=q.pop(0)
		visited[current]=1
		for v in graph[current]:
			if visited[v[0]]==0:
				q.append(v[0])
				parent[v[0]]=current
				bfs_tree[v[0]]=v[1]
				visited[v[0]]=1
	for i in range(n+1):
		visited[i]=0
	que=[1]
	level[1]=0
	while que:
		curr=que.pop(0)
		if visited[curr]==0:
			visited[curr]=1
			for v in graph[curr]:
				if visited[v[0]]==0:
					gobar[v[0]]=bfs_tree[v[0]]^gobar[curr]
					level[v[0]]=level[curr]+1
					que.append(v[0])
	fun=[]
	for i in bfs_tree:
		fun.append(i,bfs_tree[i])
	fun.sort(key=lambda x:x[1],reverse=True)
	preprocess()
	m=input()
	if n>1000000:
		for y in range(m):
			u,v,k=map(int,raw_input().split())
			res=0
			lc=lca(u,v)
			res^=gobar[u]^gobar[v]^gobar[lc]^gobar[lc]
			print res
	else:
		for y in range(m):
			u,v,k=map(int,raw_input().split())
			res=0
			lc=lca(u,v)
			if k>=ma:
				res^=gobar[u]^gobar[v]^gobar[lc]^gobar[lc]
			else:
				if u==root or v==root:
					if u==root and v!=root:
						x=v
						while x!=root:
							if bfs_tree[x]<=k:
								res^=bfs_tree[x]
							x=parent[x]
					elif u!=root and v==root:
						x=u
						while x!=root:
							if bfs_tree[x]<=k:
								res^=bfs_tree[x]
							x=parent[x]
				
				else:	
					x=u
					while x!=lc:
						if bfs_tree[x]<=k:
							res^=bfs_tree[x]	
						x=parent[x]
					x=v
					while x!=lc:
						if bfs_tree[x]<=k:
							res^=bfs_tree[x]
						x=parent[x]
			print res

