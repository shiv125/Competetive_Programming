n=input()
graph={}
for i in range(n):
	graph[i]=[]
for i in range(n-1):
	u,v=map(int,raw_input().split(" "))
	u=u-1
	v=v-1
	graph[u].append(v)
	graph[v].append(u)
color=map(int,raw_input().split(" "))
#i is root
c=1
t=0
temp=0
for i in range(n):
	temp=0
	if temp==0:
		
		for k in graph:
			if k!=i:
				for m in graph[k]:
					if (m!=i):
						
						if ((color[m]!=color[k]) and (graph[k]!=[i])):
							c=0
							t=0
							temp=1
						else:
							t+=1
		if t==2*(n-len(graph[i])):
			c=1
			r=i
			break
res=-1
for j in graph:
	if len(graph[j])==n-1:
		res=j
if c==1:
	print "YES"
	print r+1
elif c==0 and res!=-1:
	print "YES"
	print res+1
else:
	print "NO"
			
