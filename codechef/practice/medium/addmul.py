mod=10**9+7
t=input()
while t>0:
	t-=1
	n=input()
	arr=map(int,raw_input().split())
	temp=1
	sum_=0
	total=arr[n-1]
	mul=arr[n-1]
	res=arr[n-1]
	for i in range(n-2,-1,-1):
		total=(res+sum_+temp*arr[i]+mul*arr[i])%mod
		sum_=(sum_+res)%mod
		mul=(temp*arr[i]+arr[i]*mul)%mod
		temp=(2*temp)%mod
		res=total
	print res
