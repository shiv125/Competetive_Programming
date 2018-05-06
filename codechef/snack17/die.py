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

def fun(arr,n,ki):
	flag=False
	i=binarysearch(arr,ki)
	temp=0
	if i==-1:
		count=0
		i=n
	else:
		count=n-i
	while i>0:
		temp+=ki-arr[i-1]
		if i-1<temp:
			break
		else:
			count+=1
		i-=1
	return count			
		
t=input()
for i in range(t):
	n,q=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	arr.sort()
	for m in range(q):
		ki=input()
		print fun(arr,n,ki)
     

