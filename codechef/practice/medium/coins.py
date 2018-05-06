def fun(n):
	if n not in lookup:
		if n/2+n/3+n/4>n:		
			f=fun(n/2)+fun(n/3)+fun(n/4)
			lookup[n]=f
		else:
			f=n
			lookup[n]=f

	return lookup[n]

while True:
	try:
		lookup={}
		n=input()	
		print fun(n)

	except (EOFError):
		break
