import pprint

def F(A,dx,dy,dz,size):
	B=[]
	for i in range(dx,dx+size):
		for j in range(dy,dy+size):
			for k in range(dz,dz+size):
				B.append(A[i][j][k])
	B=sorted(B)
	if (B[0] == B[size * size * size - 1]):
		return 1
	result=0
	for i in range(2):
		for j in range(2):
			for k in range(2):
				result += F(A, dx + i * size / 2, dy + j * size / 2, dz + k * size / 2,   size / 2)
	return result

N,K=map(int,raw_input().split())
n=N
A = [[[0 for k in xrange(n)] for j in xrange(n)] for i in xrange(n)]
for i in range(N):
	for j in range(N):
		arr=map(int,raw_input().split())
		for k in range(N):
			A[i][j][k]=arr[k]
count=0
B=A[:]
Z=F(A,0,0,0,N)
Y=F(A,0,0,0,N)
for i in range(N):
	for j in range(N):
		for k in range(N):
			count+=1
			if (count>K):
				break
			else:
				if (A[i][j][k]==1):
					B[i][j][k]==0
				elif (A[i][j][k]==0):
					B[i][j][k]=1
				Z=min(Z,F(B,0,0,0,N))
				Y=max(Y,F(B,0,0,0,N))
print Z,Y

			


