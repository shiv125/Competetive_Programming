t=input()
MAX=10**5+1
lookup=[0]*MAX
while t>0:
	t-=1
	n,p=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	lookup[0]=arr[0]
	for i in range(1,n):
		lookup[i]=lookup[i-1]+arr[i]
	count={}
	ma=-1
	for i in range(n):
		for j in range(i,n):
			if i!=0:
				z=(lookup[j]-lookup[i-1]+p)%p
			else:
				z=lookup[j]%p
			ma=max(ma,z)
			if z not in count:
				count[z]=1
			else:
				count[z]+=1
	print ma,count[ma]
