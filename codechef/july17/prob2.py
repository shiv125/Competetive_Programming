t=input()
while t>0:
	t-=1
	st=raw_input()
	i=0
	total=-1
	while i<len(st):
		count=0
		while i<len(st):
			if st[i]=='>':
				break
			if st[i]=='<':
				count+=1
			i+=1
		i+=1
		total=max(total,count)
	i=0
	while i<len(st):
		count=0
		while i<len(st) :
			if st[i]=='<':
				break
			if st[i]=='>':
				count+=1
			i+=1
		i+=1
		total=max(total,count)
	
	print total+1		
