k,n=map(int,raw_input().split())
a=map(int,raw_input().split())
b=map(int,raw_input().split())
partial=[0]*k
partial[0]=a[0]
for i in range(1,k)
	partial[i]+=partial[i-1]
x=set()
for i in range(k):
	x.add(b[0]-partial[i])
ans=0
for i in range(n):
	if b[i] in x:
			

