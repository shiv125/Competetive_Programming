t=1
def fun(node):
	#hole
	if len(graph[node])>=2:
			
while t>0:
	t-=1
	graph={}
	n=input()
	for i in range(1,n+1):
		graph[i]=[]
	for i in range(n-1):
		u,v=map(int,raw_input().split())
		graph[u].append(v)
		graph[v].append(u)
	print graph
	if n<=2:
		if n==1:
			print -1
		else:
			print 2
	else:
		start=1
		q=[start]
		bfs_tree={}
		parent={}
		parent[1]=1
		bfs_tree[start]=0
		while q:
			current=q.pop(0)
			#print current,
			for v in graph[current]:
				if not v in bfs_tree:
					q.append(v)
					parent[v]=current
					bfs_tree[v]=1
		bfs_tree={}
		bfs_tree[1]=0
		visited=[1]*(n+1)
		visited[0]=0
		que=[1]
		while que:
			curr=que.pop(0)
			for v in graph[curr]:
				if not v in bfs_tree:
					que.append(v)
					if visited[parent[v]]==1 and len(graph[v])>1:
						visited[v]=0
						print str(v)+'stuff'
				#	for j in graph[v]:
				#		if len(graph[j])>1:
				#			visited[v]=1
				#			print str(v)+"weird"
				#			break
				bfs_tree[v]=1
		left=sum(visited)
		print visited
		start=1
		q=[start]
		bfs_tree={}
		parent={}
		parent[1]=1
		bfs_tree[start]=0
		while q:
			current=q.pop(0)
			for v in graph[current]:
				if not v in bfs_tree:
					q.append(v)
					parent[v]=current
					bfs_tree[v]=1
		bfs_tree={}
		bfs_tree[1]=0
		visited=[1]*(n+1)
		visited[0]=0
		visited[1]=1
		que=[1]
		while que:
			curr=que.pop(0)
			for v in graph[curr]:
				if not v in bfs_tree:
					que.append(v)
					if visited[parent[v]]==1 and len(graph[v])>1:
						visited[v]=0
				bfs_tree[v]=1

		flag=0
		for i in graph[1]:
			if len(graph[i])<2:
				flag=1
				break
		if len(graph[1])==1:
			flag=1
		right=sum(visited)
		if flag:
			print left
		else:
			print min(left,right)





