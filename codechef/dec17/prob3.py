ma=10**6+1
arr=[x for x in range(2*ma)]
look=[0 for x in range(2*ma)]
arr[1]=0
for i in range(1,2*ma):
	odd=0
	even=0
	temp=arr[i]
	while temp>0:
		rem=temp%10
		if rem%2==0:
			even+=rem
		else:
			odd+=rem
		temp=temp/10
	arr[i]=abs(odd-even)
for i in range(1,2*ma):
	look[i]=look[i-1]+arr[i]
dp=[0]*(ma+2)
dp[1]=2
for i in range(2,ma):
	dp[i]=dp[i-1]+2*(look[2*i]-look[i])-arr[2*i]
t=input()
while t>0:
	t-=1
	n=input()
	print dp[n]

