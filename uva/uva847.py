while True:
	try:
		l=input()
		l=int(l)
		n=l
		res=0
		count=0
		if n<10:
			res=0
		else:
			while n>17:
				newn=n
				n=n//18
				count+=1
			if (18**count)==l:
				res=1
			elif (18**count)*9>=l:
				res=0
			else:
				res=1
		if res==0:
			print ("Stan wins.")
		else:
			print ("Ollie wins.")

	except (EOFError):
		break
