def comb(n,r):
	if (r==0 or r==n):
		return 1
	elif (r==1):
		return n
	else:
		return comb(n-1,r)+comb(n-1,r-1)
mod=10**9+7
t=input()
for i in range(t):
	n=input()
	arr=map(int,raw_input().split())
	k=max(arr)
	H={}
	for i in arr:
		if i not in H:
			H[i]=1
		else:
			H[i]+=1
	if n==1:
		print 10
	else:
		count=comb(9,k)
		for i in H:
			if H[i]>1:
				if i==1:
					count+=comb(10,H[i])
				else:
					count+=comb(9,H[i])
		print count%mod
		
