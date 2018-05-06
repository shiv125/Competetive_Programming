t=input()
result=[]
for m in range(t):
	n=input()
	arr=map(int,raw_input().split())
	max_sofar=-float("inf")
	current=0
	start=[0]*n
	end=[0]*n
	for i in range(n):
		current=max(arr[i],current+arr[i])
		max_sofar=max(max_sofar,current)
		end[i]=current
	max_sofar=-float("inf")
	current=0
	for i in range(n-1,-1,-1):
		current=max(arr[i],current+arr[i])
		max_sofar=max(max_sofar,current)
		start[i]=current
	part1=max(end)
	x=[]
	x.append(part1)
	for i in range(1,n-1):
		x.append(end[i-1]+start[i+1])
	result.append(max(x))
for i in result:
	print i
