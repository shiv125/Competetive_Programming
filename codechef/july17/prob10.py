import math
#states
#state 1-root(a) is irr and root(b) is rational
#stat 2- root(a) is rational and root(b) is rational
#state 3-root(a) is irr and root(b) is irr
#state 4 -root(a) is irr and root(b) is irr but root(c) is rational
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)
def perfectsq(a):
	b=int(math.floor(math.sqrt(a)))
	if b*b==a:
		return True
	else:
		return False
def sqroot(a):
	return int(math.floor(math.sqrt(a)))

def state1(a,rb):
	c=rb*rb-a
	x1=(-2)*rb
	print 2
	print c%mod,x1%mod,1
def state2(ra,rb):
	c=ra+rb
	print 1
	print (-c)%mod,1
def state4(a,b,rc):
	temp=a*b
	if perfectsq(temp):
		v=gcd(a,b)
		a=a/v
		b=b/v
		st=sqroot(a)+sqroot(b)
		var=st*st*v
		state1(var,rc)
	else:
		p=(-2*rc)
		q=rc*rc-(a+b)
		con=(q*q-4*a*b)%mod
		x1=(2*p*q)%mod
		x2=(p*p+2*q)%mod
		x3=(2*p)%mod
		print 4
		print con,x1,x2,x3,1

mod=10**9+7
t=input()
while t>0:
	t-=1
	n=input()
	arr=map(int,raw_input().split())
	if n==1:
		if perfectsq(arr[0]):
			res=sqroot(arr[0])
			print 1
			print (-res)%mod,1
		else:
			print 2
			print (-arr[0])%mod,0,1
	elif n==2:
		a=arr[0]
		b=arr[1]
		if perfectsq(a) and perfectsq(b):
			temp=sqroot(a)+sqroot(b)
			print 1
			print (-temp)%mod,1
		elif perfectsq(a)==False and perfectsq(b):
			state1(a,sqroot(b))
		elif perfectsq(b)==False and perfectsq(a):
			state1(b,sqroot(a))
		else:
			c=((a-b)*(a-b))%mod
			z=(-1*2*(a+b))%mod
			d=a*b
			e=math.floor(math.sqrt(d))
			e=int(e)
			print 4
			print c,0,z,0,1
	elif n==3:
		a=arr[0]
		b=arr[1]
		c=arr[2]
		if perfectsq(a) and perfectsq(b) and perfectsq(c):
			temp=sqroot(a)+sqroot(b)+sqroot(c)
			print 1
			print (-temp)%mod,1
		elif perfectsq(a)==False and perfectsq(b) and perfectsq(c):
			temp=sqroot(b)+sqroot(c)
			state1(a,temp)

		elif perfectsq(a) and perfectsq(b)==False and perfectsq(c):
			temp=sqroot(a)+sqroot(c)
			state1(b,temp)
		elif perfectsq(a) and perfectsq(b) and perfectsq(c)==False:
			temp=sqroot(a)+sqroot(b)
			state1(c,temp)
		elif perfectsq(a)==False and perfectsq(b)==False and perfectsq(c):
			temp=sqroot(c)
			state4(a,b,temp)
		elif perfectsq(a)==False and perfectsq(b) and perfectsq(c)==False:
			temp=sqroot(b)
			state4(a,c,temp)
		elif perfectsq(a) and perfectsq(b)==False and perfectsq(c)==False:
			temp=sqroot(a)
			state4(c,b,temp)
		else:
			s1=arr[0]+arr[1]+arr[2]
			s3=arr[0]*arr[1]*arr[2]
			s2=arr[0]*arr[1]+arr[1]*arr[2]+arr[2]*arr[0]
			p=(-2)*s1
			q=(s1*s1-4*s2)
			x6=2*p
			x4=p*p+2*q
			x2=2*p*q-64*s3
			x0=q*q
			print 8
			print x0%mod,0,x2%mod,0,x4%mod,0,x6%mod,0,1
	elif n==4:
		if perfectsq(a) and perfectsq(b) and perfectsq(c) and perfectsq(d):
			temp=sqroot(a)+sqroot(b)+sqroot(c)+sqroot(d)
			print 1
			print (-temp)%mod,1
		elif 

	elif n==5:

	else:
		
