n,q=map(int,raw_input().split())
store=[]
total=0
for i in range(n):
	arr=map(int,raw_input().split())
	#ser_x=arr[0]
	#ser_y=arr[1]
	for j in range(3,len(arr)):
		store.append([arr[j],i+1,j-2])
		total+=1
store.sort(key=lambda x:x[0])
j=0
for i in range(q):
	print '?'
	z=map(int,raw_input().split())
	print '! '+str(store[j][1])+' '+str(store[j][2])
	j+=1
	if j==total:
		j=0
print 'end'
