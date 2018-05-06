n,k=map(int,raw_input().split())
m=1
r=1+k
c=1
v=1
while r!=1:
	t=1
	while (r<=n):
		t+=1
		c+=m
		print c,
		v+=1
		r+=k
#	if (v>n/k+1):
		
		
	if (r>n):
		r=r-n
		r=r+k
		if (v>n/k):
			
			m+=1
			c+=m
			print c,
			m+=1
		
print c+m,
		

		

		
	
	
		

