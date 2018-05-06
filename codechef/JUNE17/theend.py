import sys
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
def binarysearch(arr,low,high,x):
	mid=0
	while low<=high:
		if x<=arr[low]:
			return low
		if x>arr[high]:
			return -1
		mid=(low+high)/2
		if arr[mid]<x:
			if mid+1<=high and x<=arr[mid+1]:
				return mid+1
			else:
				low=mid=1
		else:
			if mid-1>=low and x>arr[mid-1]:
				return mid
			else:
				high=mid-1
	return -1
MAX=10**6+2
MAP=78498
primes=[x for x in xrange(MAX)]
for i in range(4,MAX,2):
	primes[i]=2
i=3
while i*i<MAX:
	if primes[i]==i:
		j=i*i
		while j<MAX:
			if primes[j]==j:
				primes[j]=i
			j+=i
	i+=1
all_primes=[]
prime=[True for i in range(MAX+1)]
p=2
while p*p<=MAX:	
	if prime[p]==True:
		for i in range(p*2,MAX+1,p):
			prime[i]=False
	p+=1
for p in range(2,MAX):
	if prime[p]==True:
		all_primes.append(p)
dic={}
tt=len(all_primes)
for i in range(tt):
	dic[all_primes[i]]=i
n=int(sys.stdin.readline())
arr=map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline())
lookup=[0]*n
if n>=2*10**4 and n<=10**5:
	Size=n/120
elif n<10**4 and n>=2*10**3:
	Size=n/100
else:
	Size=n/20
if Size==0:
	Size=1
dp=[[0 for x in range(Size)] for y in range(MAP)]
bucket=n/Size
for i in range(n):
	lookup[i]=[]
for i in range(n):
	elem=arr[i]
	curr=primes[elem]
	count=1
	while elem>1:
		elem=elem/primes[elem]
		if curr==primes[elem]:
			count+=1
			continue
		dp[dic[curr]][i/bucket]+=count
		lookup[i].append([curr,count])
		curr=primes[elem]
		count=1
for i in range(MAP):
	for j in range(1,Size):
		dp[i][j]+=dp[i][j-1]
for i in range(Size):
	for j in range(1,MAP):
		dp[j][i]+=dp[j-1][i]
result=[]
for i in range(m):
	L,R,X,Y=map(int,sys.stdin.readline().split())
	fi=binarysearch(all_primes,0,tt-1,X)
	si=binarysearchfloor(all_primes,0,tt-1,Y)
	ans=0
	if fi!=-1:
		l_b=(L-1)/bucket
		r_b=(R-1)/bucket
		if r_b-l_b<=1:
			for j in range(L-1,R):
				for k in range(len(lookup[j])):
					if lookup[j][k][0]>=X and lookup[j][k][0]<=Y:
						ans+=lookup[j][k][1]
					if lookup[j][k][0]>Y:
						break
		else:
			if fi!=0:
				ans+=dp[si][r_b-1]-dp[si][l_b]-(dp[fi][r_b-1]-dp[fi][l_b])
			else:
				ans+=dp[si][r_b-1]-dp[si][l_b]
			R1=(l_b+1)*bucket
			for j in range(L-1,R1):
				for k in range(len(lookup[j])):
					if lookup[j][k][0]>=X and lookup[j][k][0]<=Y:
						ans+=lookup[j][k][1]
					if lookup[j][k][0]>Y:
						break
			L2=(r_b)*bucket
			for j in range(L2,R):
				for k in range(len(lookup[j])):
					if lookup[j][k][0]>=X and lookup[j][k][0]<=Y:
						ans+=lookup[j][k][1]
					if lookup[j][k][0]>Y:
						break
	print ans
