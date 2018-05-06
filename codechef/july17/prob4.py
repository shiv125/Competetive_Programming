import heapq
t=input()
while t>0:
	t-=1
	n,d=map(int,raw_input().split())
	#total=0
	ALL=[]
	for i in range(n):
		di,ti,si=map(int,raw_input().split())
		si=-si
		ALL.append([di,si,ti])
	ALL.sort(key=lambda x:x[0])
	que=[]
	j=0
	for i in range(1,d+1):
		while j<n and ALL[j][0]==i:
			heapq.heappush(que,[ALL[j][1],ALL[j][2]])
			j+=1
		if len(que)!=0:
			a=heapq.heappop(que)
			a[1]-=1
			if a[1]!=0:
				heapq.heappush(que,a)
	total=0
	while len(que)!=0:
		temp=heapq.heappop(que)
		temp=(-temp[0])*temp[1]
		total+=temp
	print total
					

