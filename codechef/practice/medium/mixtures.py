ma=float('INF')
dp=[[ma for x in range(105)] for y in range(105)]
store=[[0 for x in range(105)] for y in range(105)]
while True:
	try:
		n=input()
		arr=map(int,raw_input().split())
		for i in range(n):	
			for j in range(n):
				store[i][j]=0
				dp[i][j]=ma
		for i in range(n):
			dp[i][i]=0
			store[i][i]=arr[i]
		for i in range(n):
			for j in range(i+1,n):
				store[i][j]=(arr[j]+store[i][j-1])%100
		for l in range(1,n+1):
			for i in range(n-l+1):
				j=i+l-1
				for k in range(i,j+1): #breaking point
					dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+store[i][k]*store[k+1][j])	
		print dp[0][n-1]
	except (EOFError):
		break
