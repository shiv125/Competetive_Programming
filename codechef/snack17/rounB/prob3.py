t=input()
for y in range(t):
	n=input()
	s1=raw_input()
	s2=raw_input()
	#arr=[[0 for x in range(2)]  for y in range(n)]
	#flag=0
	count=0
	#t1,t2=0,0
	#c1,c2=0,0
	'''for i in range(n):
		arr[i][0]=s1[i]
		arr[i][1]=s2[i]
		if s1[i]=='*':
			flag1=1
			c1+=1
			if c1==1:
				t1=i
		if s2[i]=='*':
			flag2=1
			c2+=1
			if c2==1:
				t2=i
				'''
	#ind=min(t1,t2)
	#store=arr[ind]
	first=0
	second=0
	for i in range(n):
		if s1[i]=='*':
			first+=1
		if s2[i]=='*':
			second+=1
	if first==0 or second==0:
		if first==0 and second==0:
			count=0
		elif first==0 and second>=1:
			count=second-1
		elif second==0 and first>=1:
			count=first-1
	else:
		count+=max(first,second)
	print count
'''
	if flag1 and flag2:
		for i in range(ind,n):
			if s1[i]=='*':
				first+=1
			if s2[i]=='*':
				second+=1
		first-=1
		second-=1
		count+=max(first,second)
	else:
		print 
'''
'''				
	store=arr[0]
	flag1=0
	flag2=0
	flag3=0
	if flag==0:
		for i in arr:
			if i==['*','.'] or i==['.','*'] or i==['*','*']:
				count+=1
		count-=1
	else:
		for i in arr:
			if i==['*','.'] or i==['.','*'] or i==['*','*']:
				count+=1
			if i==['*','.']:
				flag1=1
			if i==['.','*']:
				flag2=1
			if i==['*','*']:
				flag1=0
				flag2=0
			if flag1 and flag2:
				flag3+=1
		if flag3>0:
			count-=1
	if count<=0:
		print 0
	else:
		print count
				
'''



	'''
		store=[s1[ind],s2[ind]]
		if store=['*','*']:
			flag1=1
			flag2=1
		if store=['.','*']:
			flag1=0
			flag2=1
		if store=['*','.']:
			flag1=1
			flag2=0
'''
				'''
			if store==['*','*'] and arr[i]==['*','*']:
				count+=1
				flag1=1
				flag2=1
			if store==['*','.'] and arr[i]==['*','*']:
				store=arr[i]
				count+=1
				flag1=1
				flag2=1
			if store==['.','*'] and arr[i]==['*','*']:
				count+=1
				store=arr[i]
				flag1=1
				flag2=1
			if store==['*','.'] and arr[i]==['*','.']:
				count+=1
				flag1=1
			if store==['*','.'] and arr[i]==['.','*']:
				flag2=1
				if flag1:
					count+=1
					flag1=0
			if store==['.','*'] and arr[i]==['.','*']:
				count+=1
				flag2=1
			if store==['.','*'] and arr[i]==['*','.']:
				flag1=1
		'''

