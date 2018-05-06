t=1
for m in range(t):
	N,K,P=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	char=raw_input()
	curr_max=0
	head=0
	tail=0
	if K>N:
		K=N
	for i in range(K):
		curr_max+=arr[i]
	total_max=curr_max
	temp=total_max
	first=arr[0]
	last=arr[K-1]
	head=arr[0]
	tail=arr[K-1]
	lookup={}
	for i in range(N+1):
		lookup[i]=0
	lookup[curr_max]=1
	for j in range(1,N-K+1):
		last=arr[j+K-1]
		curr_max+=last-first
		lookup[curr_max]+=1
		first=arr[j]
		if total_max<curr_max:
			total_max=curr_max
	count=0
	temp2=curr_max

	for i in char:
		if i=='?':
			print total_max
		else:
			if K!=N:
				f=(K-1-count)%N
				s=(N-count-1)%N
				if arr[f]==0 and arr[s]==1:
					temp+=1
					lookup[temp]+=1
				elif arr[f]==1 and arr[s]==0:
					temp-=1
					lookup[temp]+=1
				else:
					lookup[temp]+=1
				#print f,s
				f2=(N-count-K-1)%N
				s2=(N-count-1)%N
				#print f2,s2
				if arr[f2]==0 and arr[s2]==1:
					if temp2==total_max and lookup[temp2]==1:
						total_max-=1
					lookup[temp2]-=1
					temp2-=1
				elif arr[f2]==1 and arr[s2]==0:
					lookup[temp2]-=1
					temp2+=1
				else:
					lookup[temp2]-=1
					
				total_max=max(temp,temp2,total_max)	
				#print temp, temp2, total_max
				#print lookup
				count+=1
	
