t=input()
while t>0:
	t-=1
	n=input()
	arr=map(int,raw_input().split())
	bat=[]
	cat=[]
	for i in range(n):
		bat.append(1)
		cat.append(1)
	prev={}
	prev2={}
	for i in range(n):
		prev[i]=[]
		prev2[i]=[]
	for i in range(1,n):
		prev[i].append(i)
		for j in range(i):
			if arr[i]>arr[j] and bat[i]<bat[j]+1:
				bat[i]=bat[j]+1
				prev[i].append(j)
	for i in range(n-2,-1,-1):
		prev2[i].append(i)
		for j in range(n-1,i,-1):
			if arr[i]>arr[j] and cat[i]<cat[j]+1:
				cat[i]=cat[j]+1
				prev2[i].append(j)
	c1=max(cat)
	c2=max(bat)
	print cat
	print bat
	ma=max(c1,c2)
	print prev
	print prev2
	res=ma
	visited=[0]*n
	for i in range(n):
		for j in range(n):
			if ma<=cat[i]+bat[j]:
				count=len(prev[j])
			#	print prev[j]
			#	print prev2[i]
				for p in prev2[i]:
					if p not in prev[j]:
						count+=1
				ma=max(ma,count)
	print ma
	
