t=input()
arr=map(int,raw_input().split(" "))
x=[0]*t
for j in range(t/2):
	if j%2==0:	
		x[j]=arr[t-j-1]
	else:
		x[j]=arr[j]
if t%2!=0:
	for j in range(t/2,t):
		if j%2==0:	
			x[j]=arr[t-j-1]
		else:
			x[j]=arr[j]
else:
	for j in range(t/2,t):
		if j%2!=0:	
			x[j]=arr[t-j-1]
		else:
			x[j]=arr[j]

for i in x:
	print i,
		
