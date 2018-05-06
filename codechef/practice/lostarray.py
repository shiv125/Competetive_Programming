t=input()
while t>0:	
	t-=1
	n=input()
	E,O=map(int,raw_input().split())
	arr=[0]*n
	flag=False
	even=0
	odd=0
	if O>0:
		for i in range(n):
			if O==n-i+i*(n-i):
				flag=True
				break
		if flag:
			for j in range(i):
				print 0,
			print 1,
			for j in range(i+1,n):
				print 0,
			print
		else:
			print -1
	else:
		for i in range(n):
			print 0,
		print
		
	'''
	if n<=15:
		for i in range(2**n-1):
			for k in range(n):
				if 1<<k & i:
					arr[k]=1
				else:
					arr[k]=0
			for st in range(n):
				for end in range(st,n):
					temp=0
					for it in range(st,end+1):
						temp+=arr[it]
					if temp%2==0:
						even+=1
					else:
						odd+=1
			if even==E and odd==O:
				flag=True
				break
			even=0
			odd=0
		if flag:
			print ' '.join(str(x) for x in arr)
		else:
			print -1			
	else:
		print -1
	'''
