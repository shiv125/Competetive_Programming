t=input()
while t>0:
	t-=1
	a=raw_input()
	b=raw_input()
	n=len(a)
	s=''
	for i in range(n):
		if a[i]=='B' and b[i]=='B':
			s+='W'
		else:
			s+='B'
	print s
			
