def comb(n,r):
	if (r==0 or r==n):
		return 1
	elif (r==1):
		return n
	else:
		return comb(n-1,r)+comb(n-1,r-1)
comb(500,30)
print comb(500,30)
