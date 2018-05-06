mod=10**9+7
ma=300002
f=[0 for x in range(ma)]
#level=[[0 for x in range(ma)] for y in range(ma)]
values=[0 for x in xrange(ma)]
#visited=[0 for x in xrange(ma)]
t=input()
while t>0:
	t-=1
	n,Q=map(int,raw_input().split())
	#if n>3100:
	#	break
	graph={}
	for i in range(n):
		graph[i]=[]
	for i in range(n-1):
		u,v=map(int,raw_input().split())
		u-=1
		v-=1		
		graph[u].append(v)
		graph[v].append(u)
	
	#level=[[0 for x in range(n)] for y in range(n)]
#	for i in range(n):
#		level[i]=[]
#	for i in r
	#for i in range(n+1):
	#	for j in range(n+1):
	#		level[i][j]=0

	#visited=[0]*n
	#values=[0]*n
	for i in range(n):
		values[i]=0
	#for s in range(n):
	#	for i in range(n):
	#		visited[i]=0
	#	que=[s]
	#	visited[s]=1
	#	while len(que)!=0:
	#		v=que.pop(0)
	#		for i in graph[v]:
	#			if visited[i]!=1:
	#				level[s][i]=level[s][v]+1
	#				que.append(i)
	#				visited[i]=1

	for i in range(Q):
		arr=map(int,raw_input().split())
		if len(arr)>2:
			#for i in range(2,k+1):
			#	f[i]=0
			v=arr[1]-1
			k=arr[2]
			a=arr[3]
			b=arr[4]
			f[0]=a
			f[1]=b
		#	for i in range(2,k+1):
		#		f[i]=0
			
			#print level[v]
			for m in range(2,k+1):
				f[m]=f[m-1]+f[m-2]
		#	print f
			que=[v]
			#visited[s]=1
			level={}
			level[v]=0
			#flag=1
			while len(que)!=0:
				v=que.pop(0)
				if level[v]<=k:
					values[v]+=f[level[v]]
				if level[v]==k:
					break
				for i in graph[v]:
					if i not in level:
						level[i]=level[v]+1
						que.append(i)
						#visited[i]=1
				


			#for m in range(n):
			#	d=level[v][m]
			#	if d<=k:
			#		values[m]+=f[d]
		else:
			print values[arr[1]-1]%mod


