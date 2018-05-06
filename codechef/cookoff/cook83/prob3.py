def fun(n,m):
	#n,m=map(int,raw_input().split())
	if n==1:
		return m
	elif n==2:
		if m==1:
			return 2
		elif m>=2 and m<=6:
			return 4
		else:
			if m%6==0:
				return (m/6)*4
			else:
				return ((m/6)+1)*4
	else:
		if m==1:
			return 3
		elif m>1 and m<=4:
			return 4
		else:
			return m
#t=input()
#while t>0:
	t-=1
	#n,m=map(int,raw_input().split())
for m in range(1,50):
	print fun(2,m)
