def compute(r,c,mod):
	m=max(r,c)
	n=min(r,c)
	return (n*(n+1)*(3*m-n+1)/6)%mod
mod=10**9+7
print compute(3,3,mod)
