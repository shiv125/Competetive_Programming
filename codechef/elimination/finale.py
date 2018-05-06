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
MAX=10**6+2
MAP=78498
RTMAP=281
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
sieve(MAX,all_primes)
dic={}
tt=len(all_primes)
for i in range(tt):
	dic[all_primes[i]]=i
n=input()
arr=map(int,raw_input().split())
m=input()
#dp=[[0 for x in range(n)] for y in range(281)]
lookup=[0]*n
if n>=2*10**4 and n<=10**5:
	Size=n/135
elif n<10**4 and n>=2*10**3:
	Size=n/100
else:
	Size=n/50
dp=[[0 for x in range(Size)] for y in range(MAP)]
bucket=n/Size

for i in range(n):
	elem=arr[i]
	curr=primes[elem]
	count=1
	while elem>1:
		elem=elem/primes[elem]
		if curr==primes[elem]:
			count+=1
			continue
		total+=count
#		dp[curr/281][i]+=count
		dp[curr][i/bucket]+=count
		lookup[i].append([curr,count])
		curr=primes[elem]
		count=1
for i in range(MAP):
	for j in range(1,Size):
		dp[i][j]+=dp[i][j-1]
for i in range(Size):
	for j in range(1,MAP):
		dp[i][j]+=dp[i-1][j]
segment_forest=[0]*281
for i in range(281):
	segment_forest[i]=NumArray(dp[i])
result=[]
for i in range(m):
	L,R,X,Y=map(int,raw_input().split())
	fi=binarysearch(all_primes,0,tt-1,X)
	si=binarysearchfloor(all_primes,0,tt-1,Y)
	ans=0
	if fi==-1:
		print 0
	else:
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
		l_b1=l_b+1
		r_b1=r_b-1
		ans+=dp[si][]
		
















	res=0
	curr=0
	count=0
	ans=0
	if fi!=-1:		
		if si<70 and fi<70:
			if L==1:
				if fi!=0:
					ans=dp[R-1][si]-dp[R-1][fi-1]
				else:
					ans=dp[R-1][si]
			else:
				if fi!=0:
					ans=dp[R-1][si]-dp[R-1][fi-1]-(dp[L-2][si]-dp[L-2][fi-1])
				else:
					ans=dp[R-1][si]-dp[L-2][si]
		elif fi<70 and si>=70:
			s=69
			if L==1:
				if fi!=0:
					ans=dp[R-1][s]-dp[R-1][fi-1]
				else:
					ans=dp[R-1][s]
			else:
				if fi!=0:
					ans=dp[R-1][s]-dp[R-1][fi]-(dp[L-2][s]-dp[L-2][fi])
				else:
					ans=dp[R-1][s]-dp[L-2][s]

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
						if curr<=Y and curr>=X:
							ans+=count
						curr=primes[elem]
						count=1
		elif fi>=70 and si>=70:
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
						if curr<=Y and curr>=X:
							ans+=count
						curr=primes[elem]
						count=1
	result.append(ans)
for i in result:
	print i



		
		
		
		



