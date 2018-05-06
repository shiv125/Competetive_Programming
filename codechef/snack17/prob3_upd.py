#import timeit
#start = timeit.default_timer()
#corr=open("algo.txt","w+")
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
			low=mid+1
		else:
			if mid-1>=low and target>arr[mid-1]:
				return mid
			else:
				high=mid-1
def search(low,high,index):
	while low<=high and high<index and high>=0:
		mid=(high+low)/2
		if low>=zfun(low,index,ki):
			return low
		h=zfun(high,index,ki)
		if high<h:
			return -1
		zmid=zfun(mid,index,ki)
		if mid==zmid:
			return mid
		elif mid<zmid:
			low=mid+1
		else:
			if mid-1>=low and mid-1<zfun(mid-1,index,ki):
				return mid
			else:
				high=mid-1
def zfun(i,index,ki):
	return (index-i)*ki-(dp[i]-dp[index])
def fun(arr,n,ki):
	i=binarysearch(arr,ki)
	temp=0
	if i==-1:
		count=0
		i=n
	else:
		count=n-i
	temp=search(i/2,i-1,i)
	if temp==-1:
		return count
	return count+i-temp
'''
with open('testcases.txt',"r") as f:
	inp=[]
	for line in f:
		inp.append(line)
inp=[x.strip() for x in inp]
asa=len(inp)
z=0
t=10**4
while z<asa:
	n,q=map(int,inp[z].split())
	z+=1
	arr=map(int,inp[z].split())
	z+=1
	arr.sort()
	dp=[0]*(n+1)
	dp[n-1]=arr[n-1]
	count=0
	lookup={}
	for r in range(n-1,0,-1):
		dp[r-1]=arr[r-1]+dp[r]
	starter=[0]*n
	for i in range(1,n):
		ki=arr[i]
		starter[i]=search(i/2,i-1,i)
	for m in range(q):
		count=0
		ki=int(inp[z])
		tus=binarysearch(arr,ki)
		temp=0
		if tus==-1:
			count=0
			tus=n
		else:
			count=n-tus
		if tus!=0:
			tun=starter[tus-1]
			temp=search(tun,tus-1,tus)
			#temp=search(tun,tus-1,tus)
		if temp!=-1 and tus!=0:
			count=count+tus-temp
		corr.write(str(count)+"\n")
		z+=1
'''
t=input()
for i in range(t):
	n,q=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	arr.sort()
	dp=[0]*(n+1)
	dp[n-1]=arr[n-1]
	for r in range(n-1,0,-1):
		dp[r-1]=arr[r-1]+dp[r]
	starter=[0]*n
	for i in range(1,n):
		ki=arr[i]
		starter[i]=search(i/2,i-1,i)
	for m in range(q):
		count=0
		ki=input()
		tus=binarysearch(arr,ki)
		temp=0
		if tus==-1:
			count=0
			tus=n
		else:
			count=n-tus
		while tus>starter[tus-1]:
			temp+=ki-arr[tus-1]
			if tus-1<temp:
				break
			else:
				count+=1
			i-=1
		print count
		'''
		temp=0
		if tus==-1:
			count=0
			tus=n
		else:
			count=n-tus
		if tus!=0:
			tun=starter[tus-1]
			temp=search(tun,tus-1,tus)
			#temp=search(tun,tus-1,tus)
		if temp!=-1 and tus!=0:
			count=count+tus-temp
		print count
    	'''
#stop = timeit.default_timer()
#print stop-start

