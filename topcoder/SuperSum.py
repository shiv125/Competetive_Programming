def supersum(k,n):
	dp=[[0 for x in range(15)] for y in range(15)]
	for i in range(14):
		dp[0][i+1]=i+1
	for i in range(1,15):
		for j in range(1,15):
			for m in range(1,j+1):
				dp[i][j]+=dp[i-1][m]
	print dp
	return dp[k][n]

print supersum(10,10)		
