def fun(blocked,unblocked):
	prefix=[]
	flag=0
	for i in blocked:
		pref=i[0]
		for j in unblocked:
			k=1
			while k<len(i)+1:
				if pref==j[:k]:
					k+=1
					pref=i[:k]
					flag=1
				else:
					flag=0
					break
			if flag==1:
				print -1
				return
		prefix.append(pref)
	prefix.sort()
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
 
n=input()
blocked=[]
unblocked=[]
for i in range(n):
	x=raw_input()
	if x[0]=='-':
		blocked.append(x[2:])
	else:
		unblocked.append(x[2:])
	
fun(blocked,unblocked) 
