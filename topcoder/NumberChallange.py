class NumbersChallange:
	def MinNumber(self, S):
		dp=[0]*(11*10**6)
		subsetsums(arr,0,n-1,0)
		for i in range(len(dp)):
			if dp[i]==0:
				return i

	def subsetsums(arr,l,r,sum_):
		if l>r:
			dp[sum_]=1
			return
		else:
			subsetsums(arr,l+1,r,sum_+arr[l])
			subsetsums(arr,l+1,r,sum_)
	

