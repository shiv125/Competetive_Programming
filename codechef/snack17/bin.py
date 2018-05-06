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
arr=[1,1,2,3,4,5,5,5,5,6,7]
x=5
n=len(arr)
print binarysearch(arr,0,n-1,x)
