def modinverse(i,mod):
	return power(i,mod-2,mod)
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
def power1(a,b,mod):
	if b==0:
		return 1
	p=power(a,b//2,mod)%mod
	p=(p*p)%mod
	if b%2==0:
		return p
	else:
		return (p*a)%mod
t=int(input())
while t>0:
	t-=1
	n,p=map(int,raw_input().split())
	res=p-1
	if n>=p:
		print 0
	else:
		for j in range(n+1,p):
			res*=modinverse(j,p)
			res%=p
	print res
