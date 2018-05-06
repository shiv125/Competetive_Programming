n=input()
que=[]
deg=[0]*n
s=[0]*n
for v in range(n):
	dv,sv=map(int,raw_input().split())
	deg[v]=dv
	s[v]=sv
	if dv==1:
		que.append(v)
edgelist=set()
while len(que)>0:
	v=que.pop()
	temp=[v,s[v]]
	temp.sort()
	temp=tuple(temp)
	if temp[0]!=temp[1]:
		edgelist.add(temp)
	deg[s[v]]-=1
	if deg[s[v]]<1:
		que.remove(s[v])
	if deg[s[v]]==1:
		que.append(s[v])
	
	s[s[v]]=v^s[s[v]]
m=len(edgelist)
print m
for i in edgelist:
	print ' '.join(str(x) for x in i)
