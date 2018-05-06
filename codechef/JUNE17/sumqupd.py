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
	dpY=[0]*q
	dpY2=[0]*q
	dpY[q-1]=B[q-1]
	dpY2[q-1]=B[q-1]*B[q-1]
	for i in range(q-1,0,-1):
		dpY[i-1]=d[i]+B[i-1]
		dpY2[i-1]=dp[i]+B[i-1]*B[i-1]
	print dpY
	print dpY2
	i=0
	j=0
	k=0
	total=0
	while i<q and k<r and j<p:
		j+=1
		while k<r:
			if B[i]>=A[j] and B[i]>=C[k]:
				total+=(A[j]+C[k])*dpY[i]+(q-i)*A[j]*C[k]+dpY2[i]
				k+=1
			else:
				i+=1
	print total%mod
