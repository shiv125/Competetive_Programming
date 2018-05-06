def fun(l,r):
	if l==r:
		return l
	c=r
	t=1
	while c>0:
		c=c/2
		t=t*2
	t=t/2
	if l>=t:
		return fun(l-t,r-t)+t
	elif r>=2*t-1:
		return 2*t-1
	else:
		return t-1
n=input()
while n>0:
	n-=1
	l,r=map(int,raw_input().split())
	if r-l==1:
		if r%2==0:
			print l
		else:
			print r
	else:
		print fun(l,r)
