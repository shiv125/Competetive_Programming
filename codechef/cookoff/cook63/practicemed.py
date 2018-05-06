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
MAX=10**6+7
primes=[0]*MAX
MAP=78498
all_primes=[]
sieve(MAX,all_primes)
for i in range(2,MAX):
	if primes[i]==0:
		for j in range(1,MAX//i):
			if primes[i*j]==0:
				primes[i*j]=i
dic={}
tt=len(all_primes)
for i in range(tt):
	dic[all_primes[i]]=i

for i in range(2,MAX):
	if primes[i]==0:
		for j in range(1,MAX//i):
			if primes[i*j]==0:
				primes[i*j]=i
lookup=[0]*MAP
t=int(input())
while t>0:
	t-=1
	n=int(input())
	arr=list(map(int,input().split()))
	for i in range(n):
		elem=arr[i]
		curr=primes[elem]
		count=1
		while elem>1:
			elem=elem//primes[elem]
			if curr==primes[elem]:
				count+=1
				continue
			lookup[dic[curr]]+=count
			curr=primes[elem]
			count=1
	total=1
	for i in range(MAP):
		total*=(lookup[i]+1)
		lookup[i]=0
	print (total)
