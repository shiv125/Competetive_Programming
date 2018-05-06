t=input()
for i in range(t):
	N=input()
	arr=map(int,raw_input().split())
	arr=sorted(arr)
	x=arr[:N]
	y=arr[N:]
	z=[]
	ma=y[N/2]
	for m in range(N):
		z.append(str(x[m]))
		z.append(" ")
		z.append(str(y[m]))
		z.append(str(" "))
	print ma
	print ''.join(z)

