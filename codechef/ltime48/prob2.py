n=input()
parents=map(int,raw_input().split())
costs=map(int,raw_input().split())
cost=[0]*n
cost[0]=1
for i in range(1,n):
	temp=10**9
	sum_=0
	curr=i+1
	temp=min(temp,costs[curr-1])
	sum_+=temp
	while curr!=1:
		curr=parents[curr-2]
		temp=min(temp,costs[curr-1])
		sum_+=temp
	cost[i]=sum_
print " ".join(str(x) for x in cost)


