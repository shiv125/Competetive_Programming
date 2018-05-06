n=input()
a=map(int,raw_input().split())
b=map(int,raw_input().split())
store=[]
lookup=[0]*(n+1)
lookup[0]=1
z=0
z1=[]
z2=[]
for i in range(n):
	if a[i]!=b[i]:
		store.append(i)
if len(store)==1:
	for i in range(n):
		if i!=store[0]:
			lookup[a[i]]=1
	for i in range(n+1):
		if lookup[i]==0:
			z=i
			break
	for i in range(store[0]):
		print a[i],
	print z,
	for i in range(store[0]+1,n):
		print a[i],
else:

	for i in range(store[0]+1):
		z1.append(a[i])
	for i in range(store[0]+1,n):
		z1.append(b[i])
	for i in range(store[0]+1):
		z2.append(b[i])
	for i in range(store[0]+1,n):
		z2.append(a[i])
	lookup=[0]*(n+1)
	for i in z1:
		lookup[i]+=1
	flag1=0
	for i in z1:
		if lookup[i]>1:
			flag1=1
	if flag1==1:
		print ' '.join(str(x) for x in z2)
	else:
		print ' '.join(str(x) for x in z1)

		

	

		
