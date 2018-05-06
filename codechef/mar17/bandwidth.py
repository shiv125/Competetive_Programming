import math
t=input()
result=[]
for i in range(t):
	n=input()
	mat=[[0 for x in range(n)] for y in range(n)]
	countz=0#count no. of zeros
	for i in range(n):
		inp=map(int,raw_input().split(" "))
		for i in range(n):
			if inp[i]==0:
				countz+=1
	countz=float(countz)
	d=1.0+4*countz
	sol=(-1+math.sqrt(d))/2
	k=float(n)-sol
	k=math.ceil(k)-1
	result.append(k)
for i in result:
	print int(i)
