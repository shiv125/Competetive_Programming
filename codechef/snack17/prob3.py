def binarysearch(arr,low,high,x):
	mid=0
	if x<=arr[low]:
		return low
	if x>arr[high]:
		return -1
	mid=(low+high)/2
	if arr[mid]==x:
		return mid
	elif arr[mid]<x:
		if mid+1<=high and x<=arr[mid+1]:
			return mid+1
		else:
			return binarysearch(arr,mid+1,high,x)
	else:
		if mid-1>=low and x>arr[mid-1]:
			return mid
		else:
			return binarysearch(arr,low,mid-1,x)
def zfun(i,index,ki):
	return (index-i)*ki-(dp[i]-dp[index])

def search(low,high,index):
	#mid=0
	#low=0 and high=index
	mid=(low+high)/2
	#zmid=(index-mid)*ki-(dp[mid]-dp[index])
	zmid=zfun(mid,index,ki)
	#print zmid
	if high<zfun(high,index,ki):
		return -1
	#	print "yes"
	if low>=zfun(low,index,ki):
		return low
	if mid==zmid:
		return mid
	elif mid>zmid:
		if mid-1<=zfun(mid-1,index,ki):
			return mid
		else:
			return search(low,mid-1,index)
	else:
		#print str(mid)+'sdf'
		if mid+1>=zfun(mid+1,index,ki):
			#print str(zfun(mid+1,index,ki))+"hey"
			return mid
		else:
			return search(mid+1,high,index)
	
		
def fun(arr,n,ki):
	flag=False
	i=binarysearch(arr,0,n-1,ki)
	#for i in range(n):
	#	if arr[i]>=ki:
	#		flag=False
	#		break
	#	else:
	#		flag=True
	temp=0
	if i==-1:
		count=0
		i=n
	else:
		count=n-i
	#print count
	temp=search(0,i-1,i)
	#print temp
	if temp==-1:
		return count
	if flag:
		return count+i-temp
	return count+i-temp-1
	'''	
	te=binarysearch(new,0,n-1,ki)
	te=z[te][0]
	if te==n-1:
		return 0
	return n-te-count
	'''
'''
	while i>0:
		temp+=ki-arr[i-1]
		if i<temp:
			break
		else:
			count+=1
		i-=1

	return count			
'''			
t=input()
result=[]
for i in range(t):
	n,q=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	arr.sort()
	dp=[0]*(n+1)
	dp[n-1]=arr[n-1]
	for r in range(n-1,0,-1):
		dp[r-1]=arr[r-1]+dp[r]
	z=[0]*n
	dp[n]=0
	for r in range(n):
		z[r]=(r+dp[r])/(n-r)
	z=enumerate(z)
	z=sorted(z,key=lambda x:x[1])
	new=[]
	for i in range(n):
		new.append(z[i][1])
	for m in range(q):
		ki=input()
		result.append(fun(arr,n,ki))
for i in result:
	print i         
