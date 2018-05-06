def gcd(a,b):
	if (b==0):
		return a
	else:
		return gcd(b,a%b)
def gcd1(a,b,c):
	return gcd(a,gcd(b,c))
a=input()
b=input()
c=input()
gcd1(a,b,c)
print gcd1(a,b,c)


