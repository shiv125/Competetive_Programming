t=input()
while t>0:
	count=[0]*(10**5+1)
	dic=[0]*(10**5+1)
	for i in range(10**5+1):
		dic[i]=[]
	t-=1
	n=input()
	A=map(int,raw_input().split())
	B=[0]*n
	for i in range(n):
		count[A[i]]+=1
		dic[A[i]].append(i)
	identicals={}
	distincts={}
	for i in range(n):
		if count[A[i]]==2:
			if A[i] not in identicals:
				identicals[A[i]]=1
		else:
			if A[i] not in distincts:
				distincts[A[i]]=1
	identical=[]
	distinct=[]
	for i in identicals:
		identical.append(i)
	for i in distincts:
		distinct.append(i)
	if len(identical)>1 and len(distinct)>1:
		for i in range(len(identical)-1):
			a,b=dic[identical[i]]
			#c,d=dic[identical[i+1]]
			B[a]=identical[i+1]
			B[b]=B[a]
		a,b=dic[identical[len(identical)-1]]
		B[a]=identical[0]
		B[b]=B[a]
		for i in range(len(distinct)-1):
			a=dic[distinct[i]][0]
			B[a]=distinct[i+1]
		a=dic[distinct[len(distinct)-1]][0]
		B[a]=distinct[0]
		print n
		print ' '.join(str(x) for x in B)
	elif len(identical)==0:
		if len(distinct)==1:
			print 0
			print A[0]
		else:
			print n
			for i in range(1,n):
				B[i]=A[i-1]
			B[0]=A[n-1]
			print ' '.join(str(x) for x in B)
	elif len(distinct)==0:
		if len(identical)==1:
			print 0
			print ' '.join(str(x) for x in A)
		else:
			print 2*len(identical)
			for i in range(len(identical)-1):
				a,b=dic[identical[i]]
				#c,d=dic[identical[i+1]]
				B[a]=identical[i+1]
				B[b]=B[a]
			a,b=dic[identical[len(identical)-1]]
			B[a]=identical[0]
			B[b]=B[a]
			print ' '.join(str(x) for x in B)
	elif len(distinct)==1 and len(identical)==1:
		print 2
		print A[0],A[2],A[1]
	elif len(distinct)==1 and len(identical)>1:
		for i in range(len(identical)-1):
			a,b=dic[identical[i]]
			#c,d=dic[identical[i+1]]
			B[a]=identical[i+1]
			B[b]=B[a]
		a,b=dic[identical[len(identical)-1]]
		B[a]=identical[0]
		z=dic[distinct[0]][0]
		B[z]=identical[0]
		B[b]=distinct[0]
		print n
		print ' '.join(str(x) for x in B)
	elif len(distinct)>1 and len(identical)==1:
		for i in range(len(distinct)-1):
			a=dic[distinct[i]][0]
			B[a]=distinct[i+1]
		a=dic[distinct[len(distinct)-1]][0]
		B[a]=distinct[0]
		c,d=dic[identical[0]]
		B[d]=B[dic[distinct[0]][0]]
		B[c]=B[dic[distinct[1]][0]]
		B[dic[distinct[0]][0]]=identical[0]
		B[dic[distinct[1]][0]]=identical[0]
		print n
		print ' '.join(str(x) for x in B)

		
		
	
				










