mod=10**9+7
t=input()
arr=[0]*(10**5+10)
product=[0]*(10**5+10)
while t>0:
	t-=1
	total=0
	n=input()
	z=map(int,raw_input().split())
	for i in range(n+1):
		arr[i]=z[i]
	n+=1
	pow2=1
	for i in range(n,0,-1):
		product[i]=(arr[i]*pow2)%mod
		if i<n:
			product[i]=(product[i+1]%mod+product[i]%mod)%mod
		pow2=(pow2*2)%mod
	pow2=1
	for i in range(n-1):
		if i>=2:
			pow2=(2*pow2)%mod
		elem=(arr[i]*pow2)%mod
		total=(total%mod+(product[i+1]*elem)%mod)%mod
	print total%mod

