t=input()
while t>0:
	t-=1
	M,x,y=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	lookup=[False]*101
	lookup[0]=True
	temp=x*y
	for i in range(M):
		mi=max(arr[i]-temp,0)
		ma=min(arr[i]+temp,100)
		for j in range(mi,ma+1):
			lookup[j]=True
	count=0
	for i in lookup:
		if i==False:
			count+=1
	print count
