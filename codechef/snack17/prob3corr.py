import timeit
start = timeit.default_timer()
correct=open("correct.txt","w+")
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
	if low<=zfun(low,index,ki):
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
	i=binarysearch(arr,ki)
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
	while i>0:
		temp+=ki-arr[i-1]
		if i-1<temp:
			break
		else:
			count+=1
		i-=1
	return count			
		
#t=input()
t=10**4
with open('testcases.txt',"r") as f:
	inp=[]
	for line in f:
		inp.append(line)
inp=[x.strip() for x in inp]
asa=len(inp)

z=0
result=[]
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
		ki=int(inp[z])
		result.append(fun(arr,n,ki))
		z+=1
'''
for i in range(t):
	n,q=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	arr.sort()
	for m in range(q):
		ki=input()
		result.append(fun(arr,n,ki))
for i in result:
	print i        
'''
for i in result:
	correct.write(str(i)+"\n")
stop = timeit.default_timer()
print stop-start
