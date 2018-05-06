def mpi():
	return map(int,raw_input().split())
n=input()
a=mpi()
c1=0
c2=0
for i in a:
	if i==1:
		c1+=1
	else:
		c2+=1
if c2>=c1:
	print c1
else:
	print c2+(c1-c2)/3


