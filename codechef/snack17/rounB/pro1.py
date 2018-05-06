t=input()
result=[]
for i in range(t):
	x=raw_input()
	killed_snakes=0
	res=0#0 for tie, 1 for snakes
	if len(x)==1:
		if x=='s':
			res=1
		else:
			res=-1
	else:
		j=1
		while j<len(x):
			if x[j-1]+x[j]=='sm' or x[j-1]+x[j]=='ms':
				j+=2
				killed_snakes+=1
			else:
				j+=1
		snakes=0
		mong=0
		for j in x:
			if j=='s':
				snakes+=1
			else:
				mong+=1
		z=snakes-killed_snakes-mong
		if z>0:
			res=1
		elif z==0:
			res=0
		else:
			res=-1
	result.append(res)
for i in result:
	if i==1:
		print 'snakes'
	elif i==0:
		print 'tie'
	else:
		print 'mongooses'

				
