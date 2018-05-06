n,k=map(int,raw_input().split())
a=map(int,raw_input().split())
b=map(int,raw_input().split())
if k>1:
	print "Yes"
else:
	for i in range(n):
		if a[i]==0:
			break
	
	a[i]=b[0]
	z=[]
	for j in range(n):
		z.append(a[j]) 
	a.sort()
	flag=0
	for i in range(n):
		if a[i]!=z[i]:
			flag=1
			break
	if flag==1:
		print "Yes"
	else:
		print "No"
