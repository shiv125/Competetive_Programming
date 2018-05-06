N,M=map(int,raw_input().split())
costs=map(int,raw_input().split())
Graph={}
degrees=[]
for i in range(N):
	Graph[i]=[]
for i in range(M):
	u,v=map(int,raw_input().split())
	Graph[u-1].append(v-1)
	Graph[v-1].append(u-1)
n=N
if N<=2:
	print 0
else:
	if M==N-1:
		print 0
	elif M==N*(N-1)/2:
		arr=sorted(costs)
		ind1=costs.index(arr[-1])
		ind2=costs.index(arr[-2])
		print n-2
		for i in range(n):
			if i==ind1 or i==ind2:
				continue
			print i+1,
	else:
		u=0
		for i in range(n):
			degrees.append(len(Graph[i]))
			if len(Graph[i])==n-1:
				u=i
		degrees.sort()
		k=degrees[-1]
		flag=1
		for i in range(n-1):
			if degrees[i]!=3:
				flag=0
		m1=0
		m2=10**5
		m3=0
		store=0
		z=0
		if flag and k==n-1:
			for i in range(n):
				if i!=u:
					m1+=costs[i]
			for i in range(n):
				if i!=u:
					if m2<costs[i]:
						store=m2
					m2=min(m2,costs[i])			
			print min(m1,m2+costs[u])
			if m1<=m2+costs[u]:
				for i in range(n):
					if i==u:
						continue
					print i+1,
			else:
				print u+1,store+1
		else:
			print 0


