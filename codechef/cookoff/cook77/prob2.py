def calc(count):
	res=0
	for i in range(32):
		if count[i]>0:
			res+=(1<<i)
	return res
t=input()
while t>0:
	t-=1
	n,k=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	count=[0]*32
	i=0
	j=0
	ans=0
	while i<n:
		while calc(count)<k and j<n:
			for m in range(32):
				count[m]+=arr[j]&(1<<m)
			j+=1
		if calc(count)>=k:
			ans+=n-j+1
		for m in range(32):
			count[m]-=arr[i]&(1<<m)
		i+=1
	print ans



