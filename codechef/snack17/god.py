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
	mid=(low+high)/2
	zmid=zfun(mid,index,ki)
	if high<zfun(high,index,ki):
		return -1
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
		if mid+1>=zfun(mid+1,index,ki):
			return mid
		else:
			return search(mid+1,high,index)
	
		
def fun(arr,n,ki):
	flag=False
	i=binarysearch(arr,0,n-1,ki)
	temp=0
	if i==-1:
		count=0
		i=n
	else:
		count=n-i
 
	temp=search(0,i-1,i)
	if temp==-1:
		return count
	return count+i-temp-1
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
	for m in range(q):
		ki=input()
		result.append(fun(arr,n,ki))
for i in result:
	print i          

