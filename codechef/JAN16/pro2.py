def sieve(MAX,all_primes):
	prime=[True for i in range(MAX+1)]
	p=2
	while p*p<=MAX:	
		if prime[p]==True:
			for i in range(p*2,MAX+1,p):
				prime[i]=False
		p+=1
	for p in range(2,MAX):
		if prime[p]==True:
			all_primes.append(p)
MAX=10**4+10
all_primes=[]
sieve(MAX,all_primes)
t=input()
while t>0:
	t-=1
	n=input()
	arr=map(int,raw_input().split())
	mi=1000000000000
	for gcd in all_primes:
		new_no=0
		local=0
		for i in range(n):
			if arr[i]>new_no:
				new_no=((arr[i]+gcd-1)/gcd)*gcd
			local+=new_no-arr[i]
		mi=min(mi,local)
	print mi
