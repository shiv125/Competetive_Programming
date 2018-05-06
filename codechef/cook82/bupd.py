def pri():
	ma=31625
	pre={}
	pre[2]=0
	for i in range(3,ma,2):
		for j in pre:
			if i%j==0:
				break
			if j*j>i:
				pre[i]=0
				break
	return pre
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
	for i in range(len(p)):
		while n%d==0:
			prime[d]+=1
			n //=d
		i+=1
	if n>1:
			prime[n]+=1
while True:
	try:
		n=input()
		arr=map(int,raw_input().split())
		prime={}
		mod=10**9+7
		pre=pri()
		for x in arr:
			for i in pre:
				while x%i==0:
					pre[i]+=1
					x //=i
				
		if x>1:
			pre[x]+=1
		prime=pre
#		for i in arr:
#			primes(i,prime)
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
	except (EOFError):
		break
		
