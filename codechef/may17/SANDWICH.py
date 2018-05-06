import operator as op

def mod_exp(b,e,mod):
    r = 1
    while e > 0:
        if (e&1) == 1:
            r = (r*b)%mod
        b = (b*b)%mod
        e >>= 1

    return r

# get degree of p in n! (exponent of p in the factorization of n!)
def fact_exp(n,p):
    e = 0
    u = p
    t = n
    while u <= t:
        e += t//u
        u *= p

    return e

# convert given number n into array of its base b representation
# most significant digit is at rightmost position in array
def get_base_digits(n,b):
    d = []
    while n > 0:
        d.append(n % b)
        n  = n // b

    return d

# Using Fermat's little theorem to compute nCk mod p
# considering cancelation of p in numerator and denominator
# Note: p must be prime
def fermat_binom_advanced(n,k,p):
    # check if degrees work out
    num_degree = fact_exp(n,p) - fact_exp(n-k,p)
    den_degree = fact_exp(k,p)
    if num_degree > den_degree:
        return 0

    if k > n:
        return 0

    # calculate numerator and cancel out occurrences of p
    num = 1
    for i in range(n,n-k,-1):
        cur = i
        while cur%p == 0:
            cur //= p
        num = (num*cur)%p

    # calculate denominator and cancel out occurrences of p
    denom = 1
    for i in range(1,k+1):
        cur = i
        while cur%p == 0:
            cur //= p
        denom = (denom*cur)%p

    # numerator * denominator^(p-2) (mod p)
    return (num * mod_exp(denom,p-2,p))%p

# Using Lucas' theorem to split the problem into smaller sub-problems
# In this version assuming p is prime
def lucas_binom(n,k,p):
    # get n and k in base p representation
    np = get_base_digits(n,p)
    kp = get_base_digits(k,p)

    # calculate (nCk) = (n0 choose k0)*(n1 choose k1) ... (ni choose ki) (mod p)
    binom = 1
    for i in range(len(np)-1,-1,-1):
        ni = np[i]
        ki = 0
        if i < len(kp):
            ki = kp[i]

        binom = (binom * fermat_binom_advanced(ni,ki,p)) % p

    return binom



def ncr(n,r,p):
	C=[0]*(r+1)
	C[0]=1
	for i in range(1,n+1):
		for j in range(min(i,r),0,-1):
			C[j]=(C[j]+C[j-1])%p
	return C[r]

def comb(n,r,p):
	if r==0:
		return 1
	ni=n%p
	ri=r%p
	return (comb(n/p,r/p,p)*ncr(ni,ri,p))%p
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

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
		m=n%mod
		for i in range(2,m+1,1):
			res=(res*i)%mod
		if ((n)%2>0):
			res=mod-res
		n=n/mod
	return res
#def comb(n,r,mod):
#	if countfact(n,mod)>countfact(r,mod)+countfact(n-r,mod):
#		return 0
#	return (fact(n,mod)*((inverse(fact(r,mod),mod)*inverse(fact(n-r,mod),mod))%mod))%mod
#def comb(n, r,MOD):
 #   if r > n - r:
  #      r = n - r

   # num = 1
    #den = 1
    #j = 1
    #for i in xrange(n - r + 1, n + 1):
     #   num *= i
      #  den *= j
       # j += 1

    #return (num / den) % MOD
def comb(n, r,M):
    r = min(r, n-r)
    if r == 0: return 1
    n = reduce(op.mul, xrange(n, n-r, -1))
    d = reduce(op.mul, xrange(1, r+1))
    return (n//d)%M

def first(t,r,M):
	return comb(t+r-1,t,M)
def second(m,r,M):
	return comb(r,m,M)
def first1(t,r,M):
	return lucas_binom(t+r-1,t,M)
def second1(m,r,M):
	return lucas_binom(r,m,M)

t=input()
z=t
result=[]
for i in range(t):
	N,K,M=map(int,raw_input().split())
	if N<10**6:
		if N%K==0:
			result.append(N/K)
			result.append(1)
		else:
			r=N/K
			r+=1
			t=N-r
			m=0
			count=0
			while t>0:
				x=((first(t,r,M))*(second(m,r,M)))
				if m%2!=0:
					count=(count-x)
				else:
					count=(count+x)
				m+=1
				t-=K
			result.append(r)
			result.append(count%M)
	else:
		if N%K==0:
			result.append(N/K)
			result.append(1)
		else:
			r=N/K
			r+=1
			t=N-r
			m=0
			count=0
			while t>0:
				x=((first1(t,r,M)%M)*(second1(m,r,M)%M))%M
				if m%2!=0:
					count=(count%M-x%M)%M
				else:
					count=(count%M+x%M)
				m+=1
				t-=K
			result.append(r)
			result.append(count%M)

for i in range(0,2*z-1,2):
	print result[i], 
	print result[i+1]

