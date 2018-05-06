from fractions import Fraction
mod1=10**9+7
mod2=10**9+9
def modinv(a,m):
	m0=m
	x0=0
	x1=1
	if m==1:
		return 0
	while a>1:
		q=a/m
		t=m
		m=a%m
		a=t
		t=x0
		x0=x1-q*x0
		x1=t
	if x1<0:
		x1+=m0
	return x1
t=input()
while t>0:
	t-=1
	n=input()
	num=(n*(n-1))/2
	denom=2*n-3
	a=Fraction(num,denom)
	num=a.numerator
	den=a.denominator
	mi1=modinv(den,mod1)
	res1=((num%mod1)*mi1)%mod1
	mi2=modinv(den,mod2)
	res2=((num%mod2)*mi2)%mod2
	print res1,res2
