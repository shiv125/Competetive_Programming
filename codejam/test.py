def fun(N,K):# if n is odd
	i=K
	r=N
	x=[]
	while i>0:
		x.append(i)	
		i=i/2
	y=[]
	z=[]
	for q in range(len(x)-2,-1,-1):
		z.append(x[q])
	for m in z:
		if r%2==0:
			if m%2==0:
				r=r/2
			else:
				r=r/2-1
		else:
			r=r/2
	if r%2==0:
		a=r/2
		b=r/2-1
	else:
		a=r/2
		b=r/2
	as1=max(a,b)
	as2=min(a,b)
	return as1,as2
N=18#odd
K=6
print fun(N,K)
