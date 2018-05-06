def prime(x):
	if x>=2:
		for k in range(2,x):
			if not (x%k):
				return False
	else:
		return False
	return True
n=input()
if n%2==0:
	for j in range(1,1001):
		if (prime(n*j+1)==False):
			print j
			break
	#k2=n*2+1
	#k4=n*4+1
	#if (prime(k2)):
	#	print 4
	#else:
	#	print 2
		
else:
	if n==1:
		print 3
	else:
		print 1
	
