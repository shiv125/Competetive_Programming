def lcs(a,b):
	na=len(a)
	nb=len(b)
	dp=[[0 for x in range(nb)] for y in range(na)]
	for i in range(na):
		for j in range(nb):
			if i==0 or j==0:
				if i==0 and j!=0:
					if a[i]!=b[j]:
						dp[i][j]=dp[i][j-1]
					else:
						dp[i][j]=1
				elif i==0 and j==0:
					if a[i]==b[j]:
						dp[i][j]=1
				elif i!=0 and j==0:
					if a[i]!=b[j]:
						dp[i][j]=dp[i-1][j]
					else:
						dp[i][j]=1


			else:
				if a[i]==b[j]:
					dp[i][j]=dp[i-1][j-1]+1
				else:
					dp[i][j]=max(dp[i-1][j],dp[i][j-1])
	return dp[na-1][nb-1]
				

inp=raw_input()
n=len(inp)
x=[]
for i in range(1,n):
	first=inp[0:i]
	second=inp[i:]
	x.append(lcs(first,second))
if x==[]:
	print 0
else:
	print 2*max(x)
'''
x='frank'
y='furt'
print lcs(x,y)
'''
