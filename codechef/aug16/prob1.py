t=input()
while t>0:
	t-=1
	n,m=map(int,raw_input().split())
	if (n*m)%2==0:
		print "Yes"
	else:
		print "No"
