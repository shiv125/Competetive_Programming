def sieve(MAX,all_primes):
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

MAX=10**6
primes=[0]*MAX
all_primes=[]
sieve(MAX,all_primes)
for i in range(2,MAX):
	if primes[i]==0:
		for j in range(1,MAX/i):
			if primes[i*j]==0:
				primes[i*j]=i
dic={}
tt=len(all_primes)
test=[0]*tt
for i in range(tt):
	dic[all_primes[i]]=i
n=input()
arr=map(int,raw_input().split())
m=input()

dp=[[0 for x in range(71)] for y in range(n)]
for i in range(n):
	elem=arr[i]
	curr=primes[elem]
	count=1
	total=0
	while elem>1 and primes[elem]<350:
		elem=elem/primes[elem]
		if curr==primes[elem]:
			count+=1
			continue
		total+=count
		dp[i][dic[curr]]=count
		curr=primes[elem]
		count=1
	dp[i][70]=elem

for j in range(70):
	for i in range(n-1):
		dp[i+1][j]+=dp[i][j]
for i in range(n):
	for j in range(69):
		dp[i][j+1]+=dp[i][j]

result=[]
for i in range(m):
	L,R,X,Y=map(int,raw_input().split())
	fi=binarysearch(all_primes,0,tt-1,X)
	si=binarysearchfloor(all_primes,0,tt-1,Y)
	res=0
	curr=0
	count=0
	if fi!=-1:
		for j in range(L-1,R):
			elem=arr[j]
			curr=primes[elem]
			count=1
			while elem>1:
				elem=elem/primes[elem]
				if curr==primes[elem]:
					count+=1
					continue
				test[dic[curr]]+=count
				curr=primes[elem]
				count=1
		for k in range(fi,si+1):
			res+=test[k]
		for k in range(tt):
			test[k]=0
	result.append(res)
for i in result:
	print i



		
		
		
		



