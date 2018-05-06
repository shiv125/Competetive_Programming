def ma(char,N,K):
	curr_max=0
	for i in range(K):
		curr_max+=arr[i]
	total_max=curr_max
	first=arr[0]
	last=arr[K-1]

	for j in range(1,N-K+1):
		last=arr[j+K-1]
		curr_max+=last-first
	#lookup[curr_max]+=1
		first=arr[j]
		if total_max<curr_max:
			total_max=curr_max
	return total_max

t=13
for m in range(t):
	N,K,P=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	char=raw_input()
	if K>N:
		K=N
	for i in char:
		if i=='?':
			print ma(arr,N,K)
		else:
			if K!=N:
				x=arr.pop()
				arr=[x]+arr


	
