def product(arr,n,K):
	count=0
	x=1
	while x<2**n:
		prod=1
		t=[]
		for k in range(n):
			z=1
			z=z<<k
			if x & z:
				prod=prod*arr[k]
				t.append(k)
		w=len(t)
		print t
		r=t[w-1]+1-w
		print r,w
		if prod>K:
			count+=2**r
			x=2**(t[w-1]+1)-1
			print x, count
		x+=1

	return 2**n-count-1
t=1
for m in range(t):
	N,K=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	arr=sorted(arr)
	print product(arr,N,K)				
