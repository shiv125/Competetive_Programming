def product(arr,n,K):
	count=0
	for x in range(1,2**n):
		prod=1
		for k in range(n):
			z=1
			z=z<<k
			if x & z:
				prod=prod*arr[k]
		if prod<=K:
			count+=1
	return count
t=13
for m in range(13):
	N,K=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	print product(arr,N,K)				
