import math
def sieve(MAX,prime):
	p=2
	while p*p<=MAX:	
		if prime[p]==True:
			for i in range(p*2,MAX+1,p):
				prime[i]=False
		p+=1
	prime[2]=False
MAX=10**5+10
prime=[True for i in range(MAX+1)]
sieve(MAX,prime)
def f(s):
	if s==0:
		return 0
	elif s==1:
		return 1
	elif s==2:
		return 2
	elif prime[s]:
		return 0
	else:
		mi=1000000
		fi=1
		si=1
		for i in range(1,int(math.sqrt(s))+1):
			if s%i==0:
				mi=min(mi,i+s/i)
				fi=i
				si=s/i
		return f(fi)+f(si)
s=input()
print f(s)
