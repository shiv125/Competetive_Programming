from math import sqrt
N,Q=map(int,raw_input().split())
arr=map(int,raw_input().split())
n=int(sqrt(N)+1)

i=0
has=[0]*n
for i in range(n):
	has[i]={}
dp3=[0]*(n)

temp1=0
temp2=0
for i in range(n):
	temp2=0
	for j in range(n*i,n*i+n):
		if j>=N:
			break
		
		temp1^=arr[j]
		temp2^=arr[j]
	
		if temp2 in has[i]:
			has[i][temp2]+=1
		else:
			has[i][temp2]=1
	dp3[i]=temp1
	
for j in range(Q):
	typ,i,x=map(int,raw_input().split())
	i-=1
	z=i/n
	r=i%n
	if typ==2:
		tot=0
		curr_xor=x
		for l1 in range(z):
			if curr_xor in has[l1]:
				tot+=has[l1][curr_xor]
			curr_xor=dp3[l1]^x
		new=curr_xor^x
		for l in range(z*n,i+1):
			new^=arr[l]
			if new==x:
				tot+=1
		print tot
	else:
		has[z]={}
		y=arr[i]^x
		arr[i]=x
		temp=0
		for l in range(z*n,min(z*n+n,N)):
			temp^=arr[l]
			if temp in has[z]:
				has[z][temp]+=1
			else:
				has[z][temp]=1
		for m in range(z,n):
			dp3[m]^=y
			
	
