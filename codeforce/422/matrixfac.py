import numpy as np
#res1=[[0 for xa in range(3)] for ya in range(3)]
mod=10**9+7
def power(a,b,mod):
	x=1
	y=a
	while b>0:
		if b%2==1:
			x=x*y
			if x>mod:
				x%=mod
		y=y*y
		if y>mod:
			y%=mod
		b/=2
	return x
t=input()
const=[[7],[4],[2]]
while t>0:
	t-=1
	n=input()
	if n==1:
		print 0
	elif n==2:
		print 0
	elif n==3:
		print 1
	else:
		res=[[1,0,0],[0,1,0],[0,0,1]]
		res=np.matrix(res)
		x=n-3
		A=[[1,1,1],[1,0,0],[0,1,0]]
		A=np.matrix(A)
		while x>0:
			if x%2==1:
				temp1=[[0,0,0],[0,0,0],[0,0,0]]
				res=res*A
				for i in range(3):
					for j in range(3):
						res[i,j]%=mod
			A=A*A
			for i in range(3):
				for j in range(3):
					A[i,j]=A[i,j]%mod
			x=x/2

		res1=7*res[0,0]+4*res[0,1]+2*res[0,2]
		print (power(2,n,mod)+mod-res1%mod)%mod
