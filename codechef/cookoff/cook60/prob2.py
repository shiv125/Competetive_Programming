t=input()
while t>0:
	t-=1
	N,D=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	i=N-1
	count=0
	arr.sort()
	while i>0:
		if arr[i]-arr[i-1]<D:
			count+=arr[i]+arr[i-1]
			i-=2
		else:
			i-=1
	print count
