MAX=5*(10**6)+2
mod=10**9+7
lookup={}
lookup[1]=0
#primes=[0]*MAX
#sieve(MAX,all_primes)
#for i in range(2,MAX):
#	if primes[i]==0:
#		for j in range(1,MAX/i):
#			if primes[i*j]==0:
#				primes[i*j]=i
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
def power(x,y,mod):
	res=1
	x=x%mod
	while y>0:
		if y&1:
			res=(res*x)%mod
		y=y>>1
		x=(x*x)%mod
	return res
def fun(n):
	if n not in lookup:
		lookup[n]=(((n/primes[n])*(primes[n]*(primes[n]-1))/2)%mod+fun(n/primes[n]))%mod
	return lookup[n]

t,l,r=map(int,raw_input().split())
res=0
x=power(t,1,mod)
y=t%mod
for i in range(r-l+1):
	if i>1:
		x=(x*y)%mod
		res=(res+x*fun(l+i))
	elif i==0:
		res=(res+(fun(l+i)))
	else:
		res=(res+x*(fun(l+i)))
print res%mod
