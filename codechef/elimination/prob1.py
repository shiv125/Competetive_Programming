#def dp(s,e,arr):
#	if s==e:
#		return arr[s]
#	else:
#		return dp(s,(s+e)/2,arr)+dp((s+e)/2+1,e,arr)+dp(s,(s+e)/2,arr)*dp((s+e)/2+1,e,arr)
arr=[1,1,1,1,1]
dp=[0]*5
dp[0]=1
dp[1]=3
n=5
total=[0]*5
total[0]=-1
total[1]=2
for i in range(2,n):
	if i==0:
		dp[i]=2**(i-1)*arr[i]+arr[i]*dp[i-1]+arr[i]*total[i-2]+dp[i-1]
	else:
		dp[i]=2**(i-1)*arr[i]+arr[i]*dp[i-1]+arr[i]*total[i-2]+dp[i-1]
	if i%2==0:
		total[i]-=dp[i]
	else:
		total[i]+=dp[i]
print dp
print total
print dp[n-1]
#print dp(0,len(arr)-1,arr)
