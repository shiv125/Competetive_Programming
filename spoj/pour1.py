t=input()
while t>0:
	t-=1
	a=input()
	b=input()
	c=input()
	x=min(a,b)
	y=max(a,b)
	total=1
	if c==0:
		print 0
	if c>y or c<x:
		print -1
	elif c==y or c==x:
		print 1
	else:
		if (y-c)%x==0:
			while y!=c:
				y-=x
				total+=2
			print total-1
		else:
			if c%x==0:
				while x!=c:
					x+=x
					total+=2
				print total+1
			else:
				print -1

