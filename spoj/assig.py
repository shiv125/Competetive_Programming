mat=[[0]*21]*21
dp=[0]*(1<<21)
def count(i):
	re=0
	while i>0:
		re+=(i&1)
		i >>= 1
	return re
t=input()
while t>0:
	t-=1
	n=input()
	for i in range(21):
		for j in range(21):
			mat[i][j]=0
	for i in range(n):
		temp=map(int,raw_input().split())
		for j in range(n):
			mat[i][j]=temp[j]
	for i in range((1<<21)):
		dp[i]=0
	dp[(1<<n)-1]=1
	print dp[(1<<n)-1]
	for i in range((1 << n)-1,-1,-1):
		l=i
		ind=count(l)
		for j in range(n):
			if mat[ind][j]==0 or ((i) & (1<<j))!=0:
				continue
			m=i|(1<<j)
			dp[i]+=dp[m]
#	for i in range(2200):
#		print dp[i],
	print dp[0]






