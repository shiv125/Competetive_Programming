MAX=10**6+1
dp=[0]*(MAX+10)
prime=[1 for i in range(MAX+1)]
p=2
while p*p<=MAX:	
	if prime[p]==1:
		for i in range(p*2,MAX+1,p):
			prime[i]=0
	p+=1
prime[0]=0
prime[1]=0
for i in range(1,MAX):
	dp[i]=dp[i-1]+prime[i]
a,b,k=map(int,raw_input().split())
if dp[b]-dp[a-1]<k:
	print -1
else:
	low=1
	high=b-a+1
	while low<high:
		flag=False
		mid=low+(high-low)/2
		for i in range(a,b):
			if i+mid-1>b:
				break
			if dp[i+mid-1]-dp[i-1]<k:
				flag=True
				break
		if flag:
			low=mid+1
		else:
			high=mid
	print low
			
	
	
