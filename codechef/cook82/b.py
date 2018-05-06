def inverse(x,y,mod):
	res=1
	x=x%mod
	while y>0:
		if y&1:
			res=(res*x)%mod
		y=y>>1
		x=(x*x)%mod
	return res
def primes(n,prime):
	d=2
	while d*d<=n:
		count=0
		while n%d==0:
			if d not in prime:
				prime[d]=1
			else:
				prime[d]+=1
			n //=d
		d+=1
	if n>1:
		if n not in prime:
			prime[n]=1
		else:
			prime[n]+=1
n=input()
arr=map(int,raw_input().split())
prime={}
mod=10**9+7
for i in arr:
	primes(i,prime)
flag=False
for j in prime:
	if prime[j]%n!=0:
		flag=True
		break

need={}
if flag:
	for j in prime:
		if prime[j]%(n+1)!=0:
			need[j]=(n+1)-prime[j]%(n+1)
	result=1
	for j in need:
		result=((result%mod)*(inverse(j,need[j],mod)))%mod
	print result
else:
	print "justdoit"
		
			
