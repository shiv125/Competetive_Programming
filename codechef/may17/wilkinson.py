def countfact(n,p):
	k=0
	while n>=p:
		k+=n/p
		n/=p
	return k
def power(a,b,mod):
	x=1
	y=a
	while (b>0):
		if b%2==1:
			x=x*y
			if x>mod:
				x%=mod
		y=y*y
		if y>mod:
			y%=mod
		b/=2
	return x
def inverse(n,mod):
	return power(n,mod-2,mod)
def fact(n,mod):
	res=1
	while n>0:
		#m=n%mod
		m=n%mod
		for i in range(2,m+1,1):
			res=(res*i)%mod
		n=n/mod
		if ((n)%2>0):
			res=mod-res
	return res
def comb(n,r,mod):
	if countfact(n,mod)>countfact(r,mod)+countfact(n-r,mod):
		return 0
	return (fact(n,mod)*((inverse(fact(r,mod),mod)*inverse(fact(n-r,mod),mod))%mod))%mod

n=10**12
r=1
M=10**6+7
print comb(n,r,M)

