mod=1000000007
t=input()
while t>0:
	t-=1
	p,q,r=map(int,raw_input().split())
	A=map(int,raw_input().split())
	B=map(int,raw_input().split())
	C=map(int,raw_input().split())
	A.sort()
	C.sort()
	B.sort()
	dpA=[0]*p
	dpC=[0]*r
	dpA[0]=A[0]
	dpC[0]=C[0]
	for i in range(1,p):
		dpA[i]=(dpA[i-1]%mod+A[i]%mod)%mod
	for i in range(1,r):
		dpC[i]=(dpC[i-1]%mod+C[i]%mod)%mod
	total=0
	x=0
	z=0
	c1=0
	flag=0
	for i in range(q):
		y=B[i]
		while x<p-1:
			if y>=A[x] and y<A[x+1]:
				break
			else:
				if y<A[x]:
					flag=1
					break
				if y>=A[x+1] and y>=A[x]:
					x+=1					
		if flag==1:
			flag=0
			continue
		while z<r-1:
			if y>=C[z] and y<C[z+1]:
				break
			else:
				if y<C[z]:
					flag=1
					break
				if y>=C[z+1] and y>=C[z]:
					z+=1
		if flag==1:
			flag=0
			continue
		if x==p-1:
			if y>=A[x]:
				x=p-1
			else:
				x=p
		if z==r-1:
			if y>=C[z]:
				z=r-1
			else:
				z=r
		if x!=p and z!=r:
			c1=(((z+1)*y)%mod*dpA[x])%mod+(((x+1)*(z+1))%mod*(y*y)%mod)%mod+(((x+1)*y)%mod*dpC[z])%mod+(dpA[x]*dpC[z])%mod
			#c1=(((z+1)*y)%mod*dpA[x])%mod
			#c2=((((x+1)*(z+1))%mod*(y*y)%mod)%mod+c1)%mod
			#c3=((((x+1)*y)%mod*dpC[z])%mod+c2)%mod
			#c4=((dpA[x]*dpC[z])%mod+c3)%mod
			total=(total+c1)%mod
		else:
			break
	print total

