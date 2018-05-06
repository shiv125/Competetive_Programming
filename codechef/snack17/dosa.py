def binarysearch(arr,target):
	low=0
	high=len(arr)-1
	while low<=high:
		mid=(high+low)/2
		val=arr[mid]
		if target<=arr[low]:
			return low
		if target>arr[high]:
			return -1
		if target==val:
			return mid
		elif target>val:
			if mid+1<=high and target<=arr[mid+1]:
				return mid+1
			else:
				low=mid+1
		else:
			if mid-1>=low and target>arr[mid-1]:
				return mid
			else:
				high=mid-1
def binarysearch1(arr,low,high,x):
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

def search1(low,high,index):
	while True:
		mid=(low+high)/2
		l=zfun(low,index,ki)
		h=zfun(high,index,ki)
		if low>=l:
			return low
		if high<h:
			return -1
		if high==h:
			return high
		mid=(low+high)/2
		zmid=zfun(mid,index,ki)
		if mid==zmid:
			return mid
		elif mid<zmid:
			low=mid+1
		else:
			high=mid-1

def search(low,high,index):
	while True:
		h=zfun(high,index,ki)
		if high<h:
			return -1
		elif high>h:
			zhighn=zfun(high-1,index,ki)
			if high-1==zhighn:
				return high-1
			elif high-1<zhighn:
				return high
		else:
			return high
		if low>=zfun(low,index,ki):
			return low
		mid=(low+high)/2
		zmid=zfun(mid,index,ki)
		if mid==zmid:
			return mid
		elif mid>zmid:
			zmidn=zfun(mid-1,index,ki)
			if mid-1==zmidn and mid-1>=low:
				return mid-1
			elif mid-1<zmidn and mid-1>=low:
				return mid
			else:
				high=mid-1
		else:
			zmidp=zfun(mid+1,index,ki)
			if mid+1>=zmidp and mid+1<=high:
				return mid+1
			else:
				low=mid+1
def fun(arr,n,ki):
	i=binarysearch(arr,ki)
	temp=0
	if i==-1:
		count=0
		i=n
	else:
		count=n-i
	temp=search(0,i-1,i)
	if temp==-1:
		return count
	return count+i-temp
t=input()
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
	#	tus=binarysearch(arr,ki)	
		print fun(arr,n,ki)
