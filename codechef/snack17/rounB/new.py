t=input()
result=[]
for y in range(t):
	n=input()
	s1=raw_input()
	s2=raw_input()
	count=0
	first=0
	second=0
	store=[s1[0],s2[0]]
	arr=[[0 for x in range(2)]  for p in range(n)]
	z1,z2=0,0
	t1,t2=0,0
	for i in range(n):
		arr[i][0]=s1[i]
		arr[i][1]=s2[i]
		if s1[i]=='*':
			first+=1
			z1+=1
			if z1==1:
				t1=i
		if s2[i]=='*':
			second+=1
			z2+=1
			if z2==1:
				t2=i
	ind=min(t1,t2)
	flag1=0
	flag2=0
	if first==0 or second==0:
		if first==0 and second==0:
			count=0
		elif first==0 and second>=1:
			count=second-1
		elif second==0 and first>=1:
			count=first-1
	else:
		store=[s1[ind],s2[ind]]
		i=ind+1
		d=0
		while i<n:
			if store==['*','.']:
				if arr[i]==['.','*']:
					d+=1
					store=['*','*']
				if arr[i]==['*','*']:
					store=['*','*']
			elif store==['.','*']:
				if arr[i]==['*','.']:
					d+=1
					store=['*','*']
				if arr[i]==['*','*']:
					store=['*','*']
			elif store==['*','*']:
				store=arr[i]
			elif store==['.','.']:
				store=arr[i]
			i+=1
		for i in range(ind+1,n):
			if arr[i]!=['.','.']:
				count+=1
		count=count-d+1	
	result.append(count)
for i in result:
	print i

