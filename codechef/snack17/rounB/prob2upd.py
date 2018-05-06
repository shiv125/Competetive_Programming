def transition(arr,j,k):
	global total
	if j<0 or k<0 or j==len(arr) or k==len(arr[0]):
		return 
	if check[j][k]:
		return 
	if (arr[j][k]!=max_):
		arr[j][k]=max_
		total+=1
		print total
		transition(arr,j,k)
	else:
		check[j][k]=True
		transition(arr,j-1,k)#
		transition(arr,j-1,k-1)
		transition(arr,j,k+1)#
		transition(arr,j+1,k+1)#
		transition(arr,j,k-1)#
		transition(arr,j-1,k+1)#
		transition(arr,j+1,k-1)#
		transition(arr,j+1,k)#
		return
	
t=input()
result=[]
for i in range(t):
	n,m=map(int,raw_input().split())
	arr=[[0 for x in range(m)] for y in range(n)]
	print arr
	for j in range(n):
		arr[j]=map(int,raw_input().split())
	max_=0
	total=0
	#print len(arr)
	#print len(arr[0])
	for j in range(n):
		max_=max(max(arr[j]),max_)
	check=[[False for j in range(m)] for y in range(n)]
	for j in range(n):
		for k in range(m):
			if arr[j][k]==max_:
				transition(arr,j,k)
	print check
	print arr
	print total
