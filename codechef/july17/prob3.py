t=input()
while t>0:
	t-=1
	n,b=map(int,raw_input().split())
	ma=-1
	temp=(n/(2*b))
	for k in range(max(0,temp-100),min(temp+100,n)):
		if (n-b*k)<=n and (n-b*k)>=0:
			ma=max(ma,k*(n-b*k))
	print ma

