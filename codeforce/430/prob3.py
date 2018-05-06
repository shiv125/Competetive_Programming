n=input()
arr=map(int,raw_input().split())
graph={}
for i in range(n):
	graph[i]=[]
for i in range(n):
	x,y=map(int,raw_input().split())
	graph[x].append([y,0])
	graph[y].append([x,0])
stack=[1]
visited=[]
for i in range(n+1):
	visited.append(False)
while (len(stack)>0):
	s=stack.pop()
	if (visited[s]==False):
		visited[s]=True
	for i in graph[s]:
		v=i[0]
		if visited[v]==False:
			stack.append(v)
