def binarysearch(arr,x):
	low=0
	high=len(arr)-1
	while low<=high:
		mid=(low+high)/2
		if arr[mid]==x:
			return 1
		elif arr[mid]>x:
			high=mid-1
		else:
			low=mid+1
	return 0
n=input()
arr=[]
for i in range(n):
	arr.append(input())	
count1={}
count2={}
for f in range(n):
	for g in range(f+1,n):
		for d in range(n):
			if arr[d]!=0:
				elem=(arr[f]+arr[g])*arr[d]
				if elem not in count1:
					count1[elem]=2
				else:
					count1[elem]+=2
				#res1.append((arr[f]+arr[g])*arr[d])
for f in range(n):
	for d in range(n):
		if arr[d]!=0:
			elem=2*arr[f]*arr[d]
			if elem not in count1:
				count1[elem]=1
			else:
				count1[elem]+=1
for a in range(n):
	for b in range(a+1,n):
		for c in range(n):
			elem=arr[a]*arr[b]+arr[c]
			if elem not in count2:
				count2[elem]=2
			else:
				count2[elem]+=2
for a in range(n):
	for c in range(n):
		elem=arr[a]*arr[a]+arr[c]
		if elem not in count2:
			count2[elem]=1
		else:
			count2[elem]+=1
#res2.sort()
count=0
for i in count1:
	if i in count2:
		count+=count2[i]*count1[i]
print count

