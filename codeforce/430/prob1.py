l,r,x,y,k=map(int,raw_input().split())
#0<n<=y-x
flag=0
for m in range(r-l+1):
	t=((m-k*x+l)/k)
	if (t*k==m-k*x+l):
		if t>=0 and t<=y-x:
			flag=1
			break
if flag:
	print "YES"
else:
	print "NO"
