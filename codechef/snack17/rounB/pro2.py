t=input()
result=[]
for i in range(t):
	n,m=map(int,raw_input().split())
	arr=[[0 for x in range(n)] for y in range(m)]
	for j in range(n):
		arr[j]=map(int,raw_input().split())
	max_=0
	for j in range(n):
		max_=max(max(arr[j]),max_)
	lookup=[]
	top=1000
	bottom=1000
	left=1000
	right=1000
	for j in range(n):
		for k in range(m):
			if arr[j][k]==max_:
				lookup.append([j,k])
	print lookup
	for j in lookup:
		top=min(top, j[0])
		bottom=min(bottom,n-1-j[0])
		left=min(left,j[1])
		right=min(right,m-1-j[1])
	print left,right,top,bottom
	result.append(max(top,bottom,left,right))

for i in result:
	print i
