t=input()
result=[]
for i in range(t):
	n=input()
	arr=map(int,raw_input().split())
	c1=0
	c2=n-1
	t=0
	t1=0
	t2=0
	while c1<c2 and c1<n:
		while c1<n and c1<c2:
			if arr[c1]>=t1+1:
				c1+=1
				t1+=1
				break
			else:
				c1+=1
		while c2>0 and c1<c2:
			if arr[c2]>=t2+1:
				c2-=1
				t2+=1
				break
			else:
				c2-=1
	count=0
	ele=1
	flag=0
	if t1==t2:
		for m in range(n):
			if ele==t1+1:
				flag=1
				break
			if arr[m]>=ele:
				ele+=1
		for p in range(m,n):
			if ele==0:
				break
			if arr[p]>=ele:
				ele-=1
		if ele!=0:
			flag=0
		if flag!=0:
			t1=t1+1
	t=max(t1,t2)
	z= sum(arr)-t*t
	if z<0:
		result.append(sum(arr)-(t-1)*(t-1))
	else:
		result.append(z)
for i in result:
	print i
