def fun(blocked,unblocked):
	prefix=[]
	flag=0
	if len(blocked)==0:
		return 0
	else:
		res=[]

		for i in blocked:
			temp=[]
			pref=i[0]
			if len(unblocked)==0:
				unblocked.append('')
			if len(unblocked)!=0:
				for j in unblocked:
					k=1
					while k<len(i)+1:
						pref=i[:k]
						if pref==j[:k]:
							k+=1
							flag=1
						else:
							flag=0
							break
					if flag==1:
						return -1
					temp.append(pref)
				temp.sort()
				prefix.append(temp[-1])
			else:
				temp.append(pref)

		prefix.sort()
		#print prefix
		store=prefix[0]
		z=[]
		z.append(store)
		count=1
		for k in range(1,len(prefix)):
			if prefix[k]!=store:
				z.append(prefix[k])
				count+=1
			store=prefix[k]
		print count
		for c in z:
			print c
	return 1

t=1
for i in range(t):
	n=input()
	blocked=[]
	unblocked=[]
	for i in range(n):
		x=raw_input()
		if x[0]=='-':
			blocked.append(x[2:])
		else:
			unblocked.append(x[2:])
	e= fun(blocked,unblocked)
	if e==-1:
		print '-1'
	elif e==0:
		print '0'


	

			
