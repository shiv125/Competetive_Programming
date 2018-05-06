import math
def binarysearch(arr,low,high,x):
	if x<=arr[low]:
		return low
	for i in range(low,high):
		if arr[i]==x:
			return i
		if arr[i]<x and arr[i+1]>=x:
			return i+1
	return -1
def binarysearchfloor(arr,low,high,x):
	if x<arr[0]:
		return -1
	high+=1
	while high-low>1:
		mid=low+(high-low)/2
		if arr[mid]<=x:
			low=mid
		else:
			high=mid
	return low
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
	return prime
def sumdivisors(n):
	res=0
	for i in range(2,int(math.floor(math.sqrt(n)))+1):
		if n%i==0:
			if i==n/i:
				res+=i
			else:
				res+=i+n/i
	elem=res+n+1
	curr=primes[elem]
	count=1
	total=0
	d=elem
	#if elem<10:
	#	print prime[1],prime[2],prime[4]
	while elem>1:
		elem=elem/primes[elem]
		if curr==primes[elem]:
			count+=1
			continue
		total+=1
		curr=primes[elem]
		count=1
#	if n<11:
#		print total
	flag=0
	val=d
	if prime[total]:
		flag=1
	return flag,val

MAX=10**5+1
all_num=[False]*MAX
#primes=[0]*(10*MAX+2)
all_primes=[]
prime=sieve(MAX,all_primes)
MAP=10**6+2
primes=[x for x in range(MAP)]
for i in range(4,MAP,2):
	primes[i]=2
i=3
while i*i<MAP:
	if primes[i]==i:
		j=i*i
		while j<MAP:
			if primes[j]==j:
				primes[j]=i
			j+=i
	i+=1
prime[1]=False
prime[0]=False

for j in range(2,320):
	i=j*j
	while i<MAX:
		all_num[i]=True
		i+=j*j
square_nums=[]
for i in range(1,MAX):
	if all_num[i]==False:
		square_nums.append(i)
final=[]
result=[]
#for i in range(100):
#	print square_nums[i],
#print
for i in range(len(square_nums)):
	flag,val=sumdivisors(square_nums[i])
	if flag:
		final.append(square_nums[i])
		result.append(val)
#for i in range(square_nums)
#for i in range(100):
#	print final[i],
#print
#for i in range(100):
#	print result[i],
for i in range(1,len(result)):
	result[i]+=result[i-1]
t=input()
output=[]
ree=0
while t>0:
	t-=1
	a,b=map(int,raw_input().split())
	fi=binarysearch(final,0,len(final)-1,a)
	si=binarysearchfloor(final,0,len(final)-1,b)
	#print fi,si
	if si==-1 or fi==-1:
		ree=0
	else:
		if fi>si:
			if b==final[si]:
				ree=result[si]
			else:
				ree=0
		else:
			if fi==0:
				ree=result[si]
			else:
				ree=result[si]-result[fi-1]
	output.append(ree)
for i in output:
	print i

