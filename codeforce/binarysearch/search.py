def binarysearchceil(arr,low,high,x):
	mid=0
	if x<=arr[low]:
		return low
	if x>arr[high]:
		return -1
	mid=(low+high)/2
	if arr[mid]<x:
		if mid+1<=high and x<=arr[mid+1]:
			return mid+1
		else:
			return binarysearch(arr,mid+1,high,x)
	else:
		if mid-1>=low and x>arr[mid-1]:
			return mid
		else:
			return binarysearch(arr,low,mid-1,x)

def binarysearchfloor(arr,low,high,x):
	mid=0
	while low<=high:
		if low>high:
			return -1
		if x>=arr[high]:
			return high
		mid=(low+high)/2
		if arr[mid]==x:
			return mid
		if mid>0 and arr[mid-1]<=x and x<arr[mid]:
			return mid-1
		if x<arr[mid]:
			high=mid-1
		if x>arr[mid]:
			low=mid+1
	return -1
