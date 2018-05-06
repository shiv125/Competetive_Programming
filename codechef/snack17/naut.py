import timeit
start = timeit.default_timer()
corr=open("algo.txt","w+")
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
	if low not in lookup:
		lookup[low]=zfun(low,index,ki)
	if mid not in lookup:	
		lookup[mid]=zfun(mid,index,ki)
	if high not in lookup:
		lookup[high]=zfun(high,index,ki)
	if high-1 not in lookup:
		lookup[high-1]=zfun(high-1,index,ki)
	if mid-1 not in lookup:
		lookup[mid-1]=zfun(mid-1,index,ki)
	if mid+1 not in lookup:
		lookup[mid+1]=zfun(mid+1,index,ki)
	if high<lookup[high]:
		return -1
	elif high>lookup[high]:
		if high-1==lookup[high-1]:
			return high-1
		elif high-1<lookup[high-1]:
			return high
	else:
		return high
	if low>=lookup[low]:
		return low
	if mid==lookup[mid]:
		return mid
	elif mid>lookup[mid]:
		if mid-1==lookup[mid-1] and mid-1>=low:
			return mid-1
		elif mid-1<lookup[mid-1] and mid-1>=low:
			return mid
		else:
			return search(low,mid-1,index)
	else:
		if mid+1>=lookup[mid+1] and mid+1<=high:
			return mid+1
		else:
			return search(mid+1,high,index)


def fun(arr,n,ki,lookup):
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
	return count+i-temp
#t=input()
t=5
with open('testcases.txt',"r") as f:
	inp=[]
	for line in f:
		inp.append(line)
inp=[x.strip() for x in inp]
asa=len(inp)
result=[]
z=0
while z<asa:
	n,q=map(int,inp[z].split())
	z+=1
	arr=map(int,inp[z].split())
	z+=1
	arr.sort()
	dp=[0]*(n+1)
	dp[n-1]=arr[n-1]
	for r in range(n-1,0,-1):
		dp[r-1]=arr[r-1]+dp[r]
	for m in range(q):
		lookup={}
		ki=int(inp[z])
		result.append(fun(arr,n,ki,lookup))
		z+=1

'''
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
'''
for i in result:
	corr.write(str(i)+"\n")     
stop = timeit.default_timer()
print stop-start
