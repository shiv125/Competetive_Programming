def binarysearchfloor(arr,low,high,x):
	'''
	while low<=high:
		mid=(low+high)/2
		if arr[mid]==x:
			return mid
		if arr[mid]<x:
			low=mid+1
		else:
			high=mid-1
	return -1
	'''
	if x<arr[0]:
		return -1
	while high-low>1:
		mid=low+(high-low)//2
		if arr[mid]<=x:
			low=mid
		else:
			high=mid
	
	return arr[low]
arr=[]


