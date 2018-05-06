def binarysearch(p,q):
	ma=-1
	for i in range(2*10**6):
		if q*dp[i]<=p*arr[i] and q*dp[i+1]>p*arr[i+1]:
			ma=max(ma,i)
	return ma
'''
	low=200
	high=MAX
	while low<=high:
		n=(low+high)/2
		if q*dp[n]<=p*arr[n] and q*dp[n+1]>p*arr[n+1]:
			return n
		elif q*dp[n]>p*arr[n]:
			high=low
		else:
			low=n+1
	return -1
'''
MAX=2*10**6+10
arr=[0]*MAX
def rub(n):
	z=n
	t=n
	new=0
	while n>0:
		new=new*10+n%10
		n/=10
	if new-t==0:
		arr[z]=arr[z-1]+1
	else:
		arr[z]+=arr[z-1]

for i in range(1,MAX):
	rub(i)
#primes
dp=[0]*(MAX+10)
prime=[1 for i in range(MAX+1)]
p=2
while p*p<=MAX:	
	if prime[p]==1:
		for i in range(p*2,MAX+1,p):
			prime[i]=0
	p+=1
prime[0]=0
prime[1]=0
for i in range(1,MAX):
	dp[i]=dp[i-1]+prime[i]
p,q=map(int,raw_input().split())
ma=binarysearch(p,q)
if ma==-1:
	print 'Palindromic tree is better than splay tree'
else:
	print ma

