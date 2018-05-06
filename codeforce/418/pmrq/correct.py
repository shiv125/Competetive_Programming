MAX=10**6+2
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
n=input()
arr=map(int,raw_input().split())
m=input()
lookup={}
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
		lookup[i].append([curr,count])
		curr=primes[elem]
		count=1
result=[]
for i in range(m):
	ans=0
	L,R,X,Y=map(int,raw_input().split())
	for j in range(L-1,R):
		ln=len(lookup[j])
		for e in range(ln):
			if lookup[j][e][0]>=X:
				break
		for f in range(e,ln):
			if lookup[j][f][0]<=Y:
				ans+=lookup[j][f][1]
			if lookup[j][f][0]>Y:
				break
	result.append(ans)
for i in result:
	print i 
