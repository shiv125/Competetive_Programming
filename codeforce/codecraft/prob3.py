def fact(n):
	if n==1:
		return 1
	else:
		n*fact(n-1)
H={}		
N,M=map(int,raw_input().split())
A=[]
for i in range(N):
	A=map(int,raw_input().split())[1:]
	#A.append(tuple(map(int,raw_input().split())[1:]))
	for j in A:
		if j not in H:
			H[j]=1
		else:
			H[j]+=1
	A=[]
print H	
B=sorted(A)
print B
total=1
for i in range(1,len(B)):
	count=1
	if (B[i]==B[i-1]):
		count+=1
	total*=fact(count)
print total
print A
