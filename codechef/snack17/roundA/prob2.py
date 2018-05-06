t=input()
for i in range(t):
	n=input()
	arr=map(int,raw_input().split())
	count=0
#	if n%2==0:
#		arr.pop()
#	n=len(n)
		
	for j in range(n/2):
		if arr[j]>j+1:
			count+=arr[j]-j-1	
			arr[j]=j+1
	elem=1
	for j in range(n-1,n/2-1,-1):
		if arr[j]>elem:
			count+=arr[j]-elem
			arr[j]=elem
		elem+=1
	c1=1
	c2=n
	t=0
#	print count
	t2=t+1
#	print arr
	while c1<c2 and c1<n:
		t+=1
		t2=t+1
		while c1<n-1 and c1<c2:
			if arr[c1]==t2:
				#print c1
				c1+=1
				break
			elif arr[c1]>t2:
				count+=arr[c1]-t2
				arr[c1]=t2
				c1+=1
				#print str(c1)+"as"
				break
			else:
				count+=arr[c1]
				arr[c1]=0
			#	if arr[c1]
				#print str(c1)+"fd"
				c1+=1
		while c2>0 and c1<=c2:
			c2-=1
			if arr[c2]==t:
	#			c2-=1
				break
			elif arr[c2]>t:
				count+=arr[c2]-t
				arr[c2]=t
	#			c2-=1
				#print 'd'
				break
			else:
				count+=arr[c2]
				arr[c2]=0
	#			c2-=1
	
	#print t2,c1,c2
	#print arr
	ele=1
	t2=max(arr)
#	print str(count)+'deb'
	for o in range(n):
		if arr[o]==ele and ele<t2:
			ele+=1
		elif arr[o]!=ele and ele<t2:
			count+=arr[o]
		elif ele==t2:
			break
	#print o,count,ele
	for w in range(o,n):
		if arr[w]==ele:
			ele-=1
		else:
			count+=arr[w]
#	print arr
	#print arr
	#if sum(arr)-(t+1)*(t+1)<0:
	#	count+=sum(arr)-t*t
	#else:
	#	count+=sum(arr)-(t+1)**2
	#print c1,c2,count
	#print arr
	'''
	xar=[]
	for u in arr:
		if u!=0:
			xar.append(u)
	store=1
	n=len(xar)
	print t
	print xar
	for u in range(1,n):
		if xar[u]==store:
			count+=xar[store]
			print "ab"
		elif xar[u]>t:
			count+=xar[u]
			print "av"
		store=xar[u]
#	cd=0
#	for z in range(1,n):
#		if arr[z]!=0:
#			if arr[z]<=arr[z-1]:
#				break
	n=len(xar)
			
#	for y in arr:
#		if y==0:
#			cd+=1
	#if (n)%2==0:
	#	count+=arr[z-1]
	#print arr
#	if c1!=c2:
#		count+=arr[c1]
	#elif c1==c2:
	#	if arr[c1-1]<=arr[c2]:
	#		count+=arr[c2]
	#if arr[c1-1]==
				#print "js"+str(arr[c2])
	#if arr[c1]==arr[c2]:
	#	count+=arr[c1]
	'''
	print count

