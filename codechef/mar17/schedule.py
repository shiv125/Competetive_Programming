#t=input()
def block(inp,store,N,K):
	t==K
	if K>=N/2:
		return 1
	else:
		y=sorted(store,reverse=True)
		y[0]=y[0]/2
		t-=1
		
t=1
for i in range(t):
	N,K=map(int,raw_input().split(" "))
	inp=raw_input()
	store=[]
	c=1
	for i in range(1,N):
		if inp[i]==inp[i-1] and i!=N-1:
			c+=1
		else:
			if i==N-1 and inp[i]==inp[i-1]:
				store.append(c+1)
			else:
				store.append(c)
			c=1
	if inp[N-1]!=inp[N-2]:
		store.append(1)
	t=sorted(store,reverse=True)
	
