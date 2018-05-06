t=input()
while t>0:
	t-=1
	a,b,n=map(int,raw_input().split())
	if n%2==0:
		print max(a,b)/min(a,b)
	else:
		c=a*2
		d=b
		print max(c,d)/min(c,d)
