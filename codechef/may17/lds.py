import os
def fun(blocked,unblocked):
	prefix=[]
	flag=0
	#print blocked
	#print unblocked
	if len(blocked)==0:
		print 0
		return 
	#elif len(unblocked)==0:
	#print -1
	#	return
	else:
		res=[]
 
		for i in blocked:
			temp=[]
			pref=i[0]
			##  print 'sds'
			if len(unblocked)==0:
				unblocked.append('')
			if len(unblocked)!=0:
				for j in unblocked:
					k=1
					while k<=len(i):
						pref=i[:k]
						if pref==j[:k]:
							k+=1
							flag=1
					#	print pref
						else:
							flag=0
							break
					if flag==1:
						print "-1"
						return
					temp.append(pref)
				temp.sort()
				prefix.append(temp[-1])
			else:
				temp.append(pref)
 
				
#		print prefix
		prefix.sort()
		#print prefix
		store=prefix[0]
		z=[]
		z.append(store)
		count=1
	#	print prefix
		for k in range(1,len(prefix)):
			if prefix[k]!=store:
				z.append(prefix[k])
				count+=1
			store=prefix[k]
		print count
		#z=os.path.commonprefix(z)
		#print z
		for c in z:
			print c
 
n=input()
blocked=[]
unblocked=[]
for i in range(n):
	x=raw_input()
	te=0
	for j in range(len(x)-1,1,-1):
		if x[j]==' ':
			te+=1
	x=x[:len(x)-te]
	if x[0]=='-':
		blocked.append(x[2:])
	else:
		unblocked.append(x[2:])
	
fun(blocked,unblocked)
