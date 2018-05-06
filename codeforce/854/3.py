ma=1000007
cities=100007
inf=100000000
departure={}
arrival={}
for i in range(ma):
	departure[i]=[]
	arrival[i]=[]
left_cost=[inf for x in xrange(ma)]
right_cost=[inf for x in xrange(ma)]
curr_mi=[0 for x in xrange(cities)]
def mp():
	return map(int,raw_input().split())
n,m,k=mp()
for i in range(m):
	d,f,t,c=mp()
	if f==0:
		arrival[d].append([t,c])
	else:
		departure[d].append([f,c])
mi=inf*n
for i in range(n+1):
	curr_mi[i]=inf
for i in range(0,1000001):
	for j in departure[i]:
		city,cost=j
		if curr_mi[city]>cost:
			mi=mi+cost-curr_mi[city]
			curr_mi[city]=cost
	left_cost[i]=mi
for i in xrange(n+1):
	curr_mi[i]=inf
mi=inf*n
for i in range(1000000,-1,-1):
	for j in arrival[i]:
		city,cost=j
		if curr_mi[city]>cost:
			mi=mi+cost-curr_mi[city]
			curr_mi[city]=cost
	right_cost[i]=mi
ans=inf*n
for i in range(1,1000000-k):
	ans=min(ans,left_cost[i-1]+right_cost[i+k])
if ans<inf:
	print ans
else:
	print -1



