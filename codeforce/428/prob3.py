n=input()
graph={}
child={}
prob=[1 for x in xrange(n+1)]
level=[0 for x in xrange(n+1)]
visited=[0 for x in xrange(n+1)]
for i in xrange(1,n+1):
	graph[i]=[]
	child[i]=[]
for i in xrange(n-1):
	u,v=map(int,raw_input().split())
	graph[u].append(v)
	graph[v].append(u)

que=[1]
#level=[0]*(n+1)
#level[1]=0
#parent=[1]*(n+1)
while que:
	curr=que.pop(0)
	if visited[curr]==0:
		visited[curr]=1
		for v in graph[curr]:
			if visited[v]==0:
				child[curr].append(v)
			#	if len(graph[curr])
				#prob[v]=prob[curr]*(len(graph[curr]))
				#level[v]=level[curr]+1
				que.append(v)

que=[1]
level[1]=0
for i in xrange(n+1):
	visited[i]=0
#parent=[1]*(n+1)
while que:
	curr=que.pop(0)
	if visited[curr]==0:
		visited[curr]=1
		for v in graph[curr]:
			if visited[v]==0:
				if len(child[curr])>0:
					prob[v]=prob[curr]*(len(child[curr]))
				level[v]=level[curr]+1
				que.append(v)

total=0.0
#print level
#print pro
if n==1:
	print 0.0
else:
	for i in xrange(2,n+1):
		if len(graph[i])==1:
			t=float(level[i])
			total+=t/prob[i]
	print total
#print child
