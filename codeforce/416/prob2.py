n,m=map(int,raw_input().split())
global arr
arr=map(int,raw_input().split())
y=[]
for i in range(m):
	l,r,x=map(int,raw_input().split())
	y=[]

	for e in arr:
		y.append(e)
	y[l-1:r]=sorted(y[l-1:r])
	print y
	if y[x-1]==arr[x-1]:
		print "Yes"
	else:
		print "No"
