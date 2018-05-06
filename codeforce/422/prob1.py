A,B=map(int,raw_input().split())
x=min(A,B)
res=1
for i in range(1,x+1):
	res*=i
print res
