t=input()
while (t>0):
	t-=1
	n,m=map(int,raw_input().split())
	parent=[0]*(n+1)
	weight=[0]*(n+1)
	corns=[0]*(n+1)
	for i in range(n):
		pv,wv=map(int,raw_input().split())
		parent[i+1]=pv
		weight[i+1]=wv
	index=[]
	for i in range(m):
		arr=map(int,raw_input().split())
		if len(arr)==4:
			state,q,u,x=arr
			if state==0:
				if weight[u]<

