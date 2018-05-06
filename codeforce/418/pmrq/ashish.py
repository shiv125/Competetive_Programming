import time
start=time.clock()
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
		mid=(low+high)/2
		if arr[mid]<=x:
			low=mid
		else:
			high=mid
	
	return low
	
	'''
	mid=0
	while low<=high:
		if x>=arr[high]:
			return high
		mid=(low+high)//2
		if arr[mid]==x:
			return mid
		#if mid>0 and arr[mid-1]<=x and x<arr[mid]:
		#	return mid-1
		elif x<arr[mid]:
			high=mid-1
		else:
			low=mid+1
	return -1
	'''
def binarysearch(arr,low,high,x):
	if x>arr[high]:
		return -1
	while high-low>1:
		mid=(low+high)/2
		if arr[mid]>=x:
			high=mid
		else:
			low=mid
	return high

	'''
	mid=0
	while low<=high:
		if x<=arr[low]:
			return low
		if x>arr[high]:
			return -1
		mid=(low+high)//2
		if arr[mid]==x:
			return mid
		elif arr[mid]<x:
			low=mid+1
		else:
			high=mid-1
			if mid-1>=low and x>arr[mid-1]:
				return mid
			else:
				high=mid-1
	return -1'''
with open('testc.txt',"r") as f:
	inp=[]
	for line in f:
		inp.append(line)
inp=[x.strip() for x in inp]



MAX=10**6+2
MAP=78498#max no. of primes
primes=[x for x in range(MAX)]
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
#print all_primes
tt=len(all_primes)
#print tt
for i in range(tt):
	dic[all_primes[i]]=i
n=int(inp[0])
arr=map(int,inp[1].split())
m=int(inp[2])
lookup={}
#print arr[274]
for i in range(n):
	lookup[i]=[]
dp=[[0 for x in range(n)] for y in range(785)]
#elements=[0]*n
counters={}
primary={}
for i in range(MAP):
	primary[i]=[]
	counters[i]=[]
for i in range(n):
	elem=arr[i]
	curr=primes[elem]
	count=1
	while elem>1:
		elem=elem//primes[elem]
		if curr==primes[elem]:
			count+=1
			continue
		dp[(dic[curr])/100][i]+=count
		lookup[i].append([curr,count])
		curr=primes[elem]
		count=1
for i in range(n):
	for j in lookup[i]:
		curr,count=j
		primary[dic[curr]].append(i)
		counters[dic[curr]].append(count)
for i in range(MAP):
	for j in range(1,len(counters[i])):
		counters[i][j]+=counters[i][j-1]
for i in range(785):
	for j in range(1,n):
		dp[i][j]+=dp[i][j-1]
for i in range(n):
	for j in range(1,785):
		dp[j][i]+=dp[j-1][i]
print time.clock()-start
for i in range(m):
	L,R,X,Y=map(int,inp[i+3].split())
	fi=binarysearch(all_primes,0,tt-1,X)
	si=binarysearchfloor(all_primes,0,tt-1,Y)
	ans=0
	#print fi,si
	#primary[785]
	#counters[785]
	
	if fi!=-1:
		l_b=(fi)/100
		r_b=si/100
		if r_b-l_b<=1:
			for j in range(fi,si+1):
				ln=len(primary[j])
				if ln>0:
					l1=binarysearch(primary[j],0,ln-1,L-1)
					r1=binarysearchfloor(primary[j],0,ln-1,R-1)					
				if l1!=-1:	
					if l1!=0:
						ans+=counters[j][r1]-counters[j][l1-1]
					else:
						ans+=counters[j][r1]
	
		else:
			if L!=1:
				ans+=dp[r_b-1][R-1]-dp[r_b-1][L-2]-(dp[l_b][R-1]-dp[l_b][L-2])
			else:
				ans+=dp[r_b-1][R-1]-dp[l_b][R-1]
			R1=(l_b+1)*100
			for j in range(fi,R1):
				ln=len(primary[j])
				if ln>0:
					l1=binarysearch(primary[j],0,ln-1,L-1)				
					r1=binarysearchfloor(primary[j],0,ln-1,R-1)
					if l1>r1:
						l1=-1
					if l1!=-1:	
						if l1!=0:
							ans+=counters[j][r1]-counters[j][l1-1]
						else:
							ans+=counters[j][r1]

			L2=(r_b)*100
			for j in range(L2,si+1):		
				ln=len(primary[j])
				if ln>0:
					l1=binarysearch(primary[j],0,ln-1,L-1)
					r1=binarysearchfloor(primary[j],0,ln-1,R-1)
					if l1>r1:
						l1=-1
					if l1!=-1:	
						if l1!=0:
							ans+=counters[j][r1]-counters[j][l1-1]
						else:
							ans+=counters[j][r1]
				
	#print ans				
	

print time.clock()-start
