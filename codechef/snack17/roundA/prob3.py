t=input()
for y in range(t):
	n=input()
	s1=raw_input()
	s2=raw_input()
	arr=[[0 for x in range(2)]  for y in range(n)]
#print arr[0]
	total=0
	for i in range(n):
		arr[i][0]=s1[i]
		arr[i][1]=s2[i]
		if s1[i]=='#':
			total+=1
		if s2[i]=="#":
			total+=1
	for i in range(n):
		if s1[i]=='#' or s2[i]=='#':
			break
	main_store=arr[i]
	sign=0
	count=0
	count1=0
	count2=0
	if arr[i][0]=='#':
		count+=1
		count1+=1
		count2+=1
	if arr[i][1]=="#":
		count+=1
		count1+=1
		count2+=1
	j=i+1
	store=main_store
	if main_store==['#','#']:
		sign=1
		while j<n:
			if store==['.','#']:
				if arr[j]==['.','#']:
					count1+=1
				elif arr[j]==['#','#']:
					count1+=2
					store=['#','#']
				else:
					break
			elif store==['#','.']:
				if arr[j]==['#','.']:
					count1+=1
				elif arr[j]==['#','#']:
					count1+=2
					store=['#','#']
				else:
					break
			else:
				if arr[j]==['.','#'] and sign==1:
					store=['.','#']
					count1+=1
					if sign==1:
						sign=-1
					else:
						sign=1
				elif arr[j]==['#','.'] and sign==-1:
					count1+=1
					store=['#','.']
					if sign==1:
						sign=-1
					else:
						sign=1

				elif arr[j]==['#','#']:
					count1+=2
				else:
					break
			j+=1
	#		if sign==1:
	#			sign=-1
	#		else:
	#			sign=1
		sign=-1
		j=i+1
		store=main_store
		while j<n:
			if store==['.','#']:
				if arr[j]==['.','#']:
					count2+=1
				elif arr[j]==['#','#']:
					count2+=2
					store=['#','#']
				else:
					break
			elif store==['#','.']:
				if arr[j]==['#','.']:
					count2+=1
				elif arr[j]==['#','#']:
					count2+=2
					store=['#','#']
				else:
					break
			else:
				if arr[j]==['.','#'] and sign==1:
					store=['.','#']

					count2+=1
				elif arr[j]==['#','.'] and sign==-1:
					store=['#','.']
					count2+=1
				elif arr[j]==['#','#']:
					count2+=2
				else:
					break
			if sign==1:
				sign=-1
			else:
				sign=1
			j+=1
		count=max(count1,count2)
	else:
		if main_store==['.','#']:
			sign=1
		elif main_store==['#','.']:
			sign=-1
		while j<n:
			if store==['.','#']:
				if arr[j]==['.','#']:
					count+=1
				elif arr[j]==['#','#']:
					count+=2
					store=['#','#']
				else:
					break
			elif store==['#','.']:
				if arr[j]==['#','.']:
					count+=1
				elif arr[j]==['#','#']:
					count+=2
					store=['#','#']
				else:
					break
			else:
				if arr[j]==['.','#'] and sign==1:
					count+=1
					store=['.','#']
				elif arr[j]==['#','.'] and sign==-1:
					count+=1
					store=['#','.']
				elif arr[j]==['#','#']:
					count+=2
				else:
					break
			j+=1
			if sign==1:
				sign=-1
			else:
				sign=1
	print count1,count2
	if count==total:
		print "yes"
	else:
		print "no"
#print arr
