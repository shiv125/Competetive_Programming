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
	ind=-1
	while low<=high:
		mid=low+(high-low)/2
		if arr[mid]>x:
			high=mid-1
		else:
			ind=mid
			low=mid+1
	return ind

def binarysearch(arr,low,high,x):
	ind=-1
	while low<=high:
		mid=low+(high-low)/2
		if arr[mid]<x:
			low=mid+1
		else:
			ind=mid
			high=mid-1
	return ind

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
n=int(input())
arr=map(int,raw_input().split())
m=int(input())
lookup={}
#print arr[274]
for i in range(n):
	lookup[i]=[]
dp=[[0 for x in range(n)] for y in range(200)]
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
		dp[(dic[curr])/393][i]+=count
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
for i in range(200):
	for j in range(1,n):
		dp[i][j]+=dp[i][j-1]
for i in range(n):
	for j in range(1,200):
		dp[j][i]+=dp[j-1][i]
for i in range(m):
	L,R,X,Y=map(int,raw_input().split())
	fi=binarysearch(all_primes,0,tt-1,X)
	si=binarysearchfloor(all_primes,0,tt-1,Y)
	ans=0
	#print fi,si
	#primary[200]
	#counters[200]
	if fi!=-1:
		l_b=(fi)/393
		r_b=si/393
		if r_b-l_b<=1:
			for j in range(fi,si+1):
				l1=binarysearch(primary[j],0,len(primary[j])-1,L-1)
				r1=binarysearchfloor(primary[j],0,len(primary[j])-1,R-1)					
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
			R1=(l_b+1)*393
			#for y in range(600):
			#	if 274 in primary[y]:
			#		print primary[y]
			#		print counters[y]
 
			for j in range(fi,R1):
				l1=binarysearch(primary[j],0,len(primary[j])-1,L-1)
				r1=binarysearchfloor(primary[j],0,len(primary[j])-1,R-1)
				if l1>r1:
					l1=-1
			#	print primary[j]
			#	print counters[j]
				if l1!=-1:	
					if l1!=0:
						ans+=counters[j][r1]-counters[j][l1-1]
						#print counters[j][r1],counters[j][l1-1]
					else:
						ans+=counters[j][r1]
						#print counters[j][r1]
			#print ans
			L2=(r_b)*393
			for j in range(L2,si+1):
				l1=binarysearch(primary[j],0,len(primary[j])-1,L-1)
				r1=binarysearchfloor(primary[j],0,len(primary[j])-1,R-1)
				if l1>r1:
					l1=-1
				if l1!=-1:	
					if l1!=0:
						ans+=counters[j][r1]-counters[j][l1-1]
					else:
						ans+=counters[j][r1]	
	print ans
