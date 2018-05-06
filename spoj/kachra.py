def fun(l,b):
	r=b%4
	if l==1 or l==0 or l==5 or l==6:
		return l
	elif l==2:
		if r==0:
			return 6
		elif r==1:
			return 2
		elif r==2:
			return 4
		elif r==3:
			return 8
	elif l==8:
		if r==0:
			return 6
		elif r==1:
			return 8
		elif r==2:
			return 4
		elif r==3:
			return 2
	elif l==4:
		r=b%2
		if r==0:
			return 6
		else:	
			return 4
	elif l==3:
		r=b%4
		if r==0:
			return 1
		elif r==1:
			return 3
		elif r==2:
			return 9
		elif r==3:
			return 7
	elif l==9:
		r=b%2
		if r==1:
			return 9
		else:
			return 1
	elif l==7:
		r=b%4
		if r==0:
			return 1
		elif r==1:
			return 7
		elif r==2:
			return 9
		elif r==3:
			return 3	

