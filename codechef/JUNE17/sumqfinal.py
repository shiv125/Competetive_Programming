def binarysearch(arr,low,high,x):
	mid=0
	while low<=high:
		if x<=arr[low]:
			return low
		if x>arr[high]:
			return -1
		mid=(low+high)/2
		if arr[mid]<x:
			if mid+1<=high and x<=arr[mid+1]:
				return mid+1
			else:
				low=mid=1
		else:
			if mid-1>=low and x>arr[mid-1]:
				return mid
			else:
				high=mid-1
	return -1
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
	flag=0
	x=0
	z=0
	c1=0
	c2=0
	c3=0
	c4=0
	for i in range(q):
		flag=0
		y=B[i]
		if x!=p-1:
			x=binarysearch(A,0,p-1,y)
			if x==p-1:
				if A[x]!=y:
					x-=1
		if z!=r-1:
			z=binarysearch(C,0,r-1,y)
			if z==p-1:
				if C[z]!=y:
					z-=1
		if x==-1:
			x=p-1
		elif x==0:
			if A[0]>y:
				x=p
		elif x<p-1:
			if A[x]!=y:
				x-=1
		if z==-1:
			z=r-1
		elif z==0:
			if C[z]>y:
				z=r
		elif z<r-1:
			if C[z]!=y:
				z-=1
		if x!=p and z!=r:
			if A[x]<=y and C[z]<=y:
				flag=1
		if flag:
			#1=(((z+1)*y)%mod*dpA[x])%mod+(((x+1)*(z+1))%mod*(y*y)%mod)%mod+(((x+1)*y)%mod*dpC[z])%mod+(dpA[x]*dpC[z])%mod
			c1=(((z+1)*y)%mod*dpA[x])%mod
			c2=((((x+1)*(z+1))%mod*(y*y)%mod)%mod+c1)%mod
			c3=((((x+1)*y)%mod*dpC[z])%mod+c2)%mod
			c4=((dpA[x]*dpC[z])%mod+c3)%mod
			total=(total+c4)%mod
	print total
