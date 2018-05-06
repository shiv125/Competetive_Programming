graph = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4], [2, 6], [4, 6], [8, 7], [8, 9], [9, 7]]
#graph=[[1,2],[1,3]]
cycles = []
desire=[0]*10
def function():
	global graph
	global cycles
	for edge in graph:
		for node in edge:
			#if len(cycles)>z:
			#	desire[node]+=1
			findNewCycles([node])
			#z=len(cycles)
def findNewCycles(path):
	sn=path[0]
	nn=None
	s=[]
	for edge in graph:
		n1,n2=edge
		if sn in edge:
			if n1==sn:
				nn=n2
			else:
				nn=n1
		if not visited(nn,path):
			s=[nn]
			s.extend(path)
			findNewCycles(s)
		elif len(path)>2 and nn==path[-1]:
			p=rot(path)
			ix=inver(p)
			if isNew(p) and isNew(ix):
				cycles.append(p)
def inver(path):
	return rot(path[::-1])

def rot(path):
	n=path.index(min(path))
	return path[n:]+path[:n]
def isNew(path):
	return not path in cycles
def visited(node,path):
	return node in path

function()
for i in cycles:
	for j in i:
		desire[j]+=1
print cycles
print desire

t=input()
for i in range(t):
	Graph={}
	graph=[]
	degree={}
	for j in range(n):
		degree[j]=[]
	n,m=map(int,raw_input().split())
	for j in range(Graph):
		Graph[j]=[]
	for q in range(m):
		u,v=map(int,raw_input().split())
		Graph[u].append(v)
		Graph[v].append(u)
		graph.append([u,v])
	for j in range(n):
		degree[len(Graph[j])].append(j)
	function()
	for o in cycles:
		for j in o:
			desire[j]+=1
	arr=[0]*n
	for y in range(n):
		arr[y]=len(degree[y])
		z=0
		for e in degree[y]:
			z+=desire[e]
		arr[y]-=z


	
