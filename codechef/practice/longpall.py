t=input()
while t>0:
	t-=1
	n=input()
	inp=map(str,raw_input().split())
	rev=''
	dp=[[1 for x in range(n)] for y in range(n)]
	for l in range(2,n+1):
		for i in range(n-l+1):
			j=i+l-1
			rev=''
			if len(inp[j])==2:
				rev+=inp[j][1]
				rev+=inp[j][0]
			else:
				rev=inp[j]
			if inp[i]==rev and l==2:
				dp[i][j]=2
			elif inp[i]==rev:
				dp[i][j]=dp[i+1][j-1]+2
			else:
				dp[i][j]=max(dp[i][j-1],dp[i+1][j])
	z=dp[0][n-1]
	print n-z
