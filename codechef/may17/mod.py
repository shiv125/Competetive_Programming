def pow(a,b,mod):
	x=1
	y=b
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
	return pow(n,mod-2,mod)
def comb(n,r,mod):
	return (f[n]*((inverse(f[r], mod) * inverse(f[n-r], mod)) % mod)) % mod

n=10000000000000
f=[0]*(n+1)
f[0]=1
mod=10**6+9
for i in range(1,n+1):
	f[i]=(f[i-1]*i)%mod
print comb(n,2,mod)

