def sieve(MAX):
	prime=[True for i in range(MAX+1)]
	p=2
	while p*p<=MAX:	
		if prime[p]==True:
			for i in range(p*2,MAX+1,p):
				prime[i]=False
		p+=1

	lis=[]
	for p in range(2,MAX):
		if prime[p]==True:
			lis.append(p)
	return lis
	#print str(lis[0])+'sdf'
	

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

small_primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349]
MAX=10**6
primes=[0]*MAX
all_primes=sieve(MAX)
#countprime=len(all_primes)
countprime=70
dic={}
for i in range(70):
	dic[small_primes[i]]=i
for i in range(2,MAX):
	if primes[i]==0:
		for j in range(1,MAX/i):
			if primes[i*j]==0:
				primes[i*j]=i
n=input()
arr=map(int,raw_input().split())
#arr=[18]
m=input()
dp=[[0 for x in range(71)] for y in range(n)]
lookup=[0]*n
for i in range(n):
	elem=arr[i]
	curr=primes[elem]
	count=1
	while elem>1:
		elem=elem/primes[elem]
		if curr==primes[elem]:
			count+=1
			continue
		#lookup[i].append([curr,count])
		lookup[i].append(curr)
		curr=primes[elem]
		count=1
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
#print dp
for j in range(70):
	for i in range(n-1):
		dp[i+1][j]+=dp[i][j]
#print dp
for i in range(n):
	for j in range(69):
		dp[i][j+1]+=dp[i][j]
#print dp
for i in range(m):
	ans=0
	L,R,X,Y=map(int,raw_input().split())
	for j in range(L-1,R):
		ln=len(lookup[j])
		for e in range(len(j)):
			if lookup[j][e][0]>=X:
				break
		for f in range(e,ln):
			if lookup[j][f][0]<=Y:
				ans+=lookup[j][f][1]
				break
	print ans		


	fi=binarysearch(small_primes,0,countprime-1,X)
	si=binarysearch(small_primes,0,countprime-1,Y)


	if all_primes[si]!=Y:
		si-=1		
	if fi!=-1 and Y<350:
		if L==1:
			if fi!=0:
				ans=dp[R-1][si]-dp[R-1][fi-1]
			else:
				ans=dp[R-1][si]
		else:
			ans=dp[R-1][si]-dp[R-1][fi]-(dp[L-2][si]-dp[L-2][fi1])
	if fi==-1:
		ans=0
	#print dp
	if fi!=-1 and Y>350:
		si=countprime-1
		if L==1:
			if fi!=0:
				ans=dp[R-1][si]-dp[R-1][fi]
			else:
				ans=dp[R-1][si]
		else:
			ans=dp[R-1][si]-dp[R-1][fi]-(dp[L-2][si]-dp[L-2][fi])
		for j in range(L-1,R):
			if dp[j][70]>1:
				elem=dp[j][70]
				curr=primes[elem]
				count=1
				while elem>1 and primes[elem]<=Y:
					elem=elem/primes[elem]
					if curr==primes[elem]:
						count+=1
						continue
					ans+=count
					curr=primes[elem]
					count=1
		
	print ans
		
		
		
		



