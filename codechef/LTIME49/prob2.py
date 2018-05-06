MAX=10**6+1
t=input()
count=[0]*MAX
dp=[0]*MAX
while t>0:
	t-=1
	n=input()
	C=map(int,raw_input().split())
	W=map(int,raw_input().split())
	dp[0]=W[0]
	count[0]=0
	for i in range(1,n):
		dp[i]=dp[i-1]+W[i]
		count[i]=0
	m=-1
	j=0
	flag=False
	l=0
	while j<n-1:
		for i in range(j,n):
			count[C[i]]+=1
			if count[C[i]]>1:
				flag=True
				if j!=0:
					m=max(dp[i-1]-dp[j-1],m)
				else:
					m=max(dp[i-1],m)
				for k in range(j,i+1):
					count[C[k]]-=1
				for l in range(i-1,-1,-1):
					if C[i]==C[l]:
						break
				break
			else:
				if j!=0:
					m=max(dp[i]-dp[j-1],m)
				else:
					m=max(dp[i],m)
		j=max(l+1,j+1)
		if flag==False:
			break
	print m
			
			
