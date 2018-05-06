inp=raw_input()
n=len(inp)
dp=[[0 for x in range(n)] for y in range(n)]
for i in range(n):
	dp[i][i]=1
for length in range(2,n+1):#length is length of subsequence
	for i in range(n-length+1):
		j=i+length-1
		if inp[i]==inp[j] and length==2:
			dp[i][j]=2
		elif inp[i]==inp[j]:
			dp[i][j]=dp[i+1][j-1]+2
		else:
			dp[i][j]=max(dp[i+1][j],dp[i][j-1])
t=dp[0][n-1]
print t

