def fun(a,n):
	for i in range(12):
		k=i
		flag=1
		e29=0
		for j in a:
			if k!=1 and k!=13 and k!=25:
				if j!=look[k]:
					flag=0
					break
			else:
				if j!=28 and j!=29:
					flag=0
					break
				else:					
					if e29==1:
						if j!=28:
							flag=0
							break
					if j==29:
						e29=1

			k+=1
					
		if flag:
			return 1
	return 0

				
def mpi():
	return map(int,raw_input().split())
look=[31,28,31,30,31,30,31,31,30,31,30,31,31,29,31,30,31,30,31,31,30,31,30,31,31,29,31,30,31,30,31,31,30,31,30,31]	
n=input()
a=mpi()
if fun(a,n):
	print "Yes"
else:
	print "No"
