#ma=30
def binarysearch(arr,low,high,x):
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

#lookup1={}
#lookup2={}
#for i in range(1,2**(ma/2)+1):
#	lookup1[i]=0
#for i in range(1,2**(ma/2)+1):
#	lookup2[i]=0

def product(arr,n,K):
	count=0
	arr1=[]
	arr2=[]
	if n%2!=0:
		c=n/2+1
	else:
		c=n/2
	for x in range(1,2**(n/2)):
		prod=1
		for k in range(n/2):
			z=1
			z=z<<k
			if x & z:
				prod=prod*arr[k]
#		lookup1[x]=prod
		arr1.append(prod)
	arr1.append(1)
	arr1.sort()
	arr=arr[n/2:]
	for x in range(1,2**c):
		prod=1
		for k in range(c):
			z=1
			z=z<<k
			if x & z:
				prod=prod*arr[k]
#		lookup2[x]=prod
		arr2.append(prod)
	arr2.sort()
	K=float(K)
	#print arr1
	#print arr2
	for i in range(1,len(arr1)):
		if K<arr1[i]:
			count+=1
	for i in range(len(arr1)):
		temp=K/arr1[i]
		#print temp
		temp1=int(temp)
		if temp1!=temp:
			z=binarysearch(arr2,0,len(arr2)-1,temp1+1)#find index of the element whose value is strictly greater than temp
			#print z
			if z!=-1:
				count+=len(arr2)-z
		else:
			z=binarysearch(arr2,0,len(arr2)-1,temp1+1)
			#print z
			if z!=-1:
				count+=len(arr2)-z
	#print count
	return 2**n-count-1
t=1
for m in range(1):
	N,K=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	print product(arr,N,K)				
