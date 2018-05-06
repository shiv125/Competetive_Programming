t=input()
for i in range(t):
	N,Q=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	for j in range(Q):
		a,b,c,d=map(int,raw_input().split())
		t1=sorted(arr[a-1:b])
		t2=sorted(arr[c-1:d])
		c=0
		for r in range(b-a+1):
			if t1[r]!=t2[r]:
				c+=1
		if c<=1:
			print 'YES'
		else:
			print 'NO'
