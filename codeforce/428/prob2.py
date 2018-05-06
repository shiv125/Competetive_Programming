n,k=map(int,raw_input().split())
arr=map(int,raw_input().split())
total=sum(arr)
seats=8*n
midseats=4*n
z=n
for i in range(k):
	if arr[i]>=4:
		x=arr[i]/4
		if x<=z:
			arr[i]-=x*4
			seats-=4*x
			z-=x
		else:
			arr[i]-=z*4
			seats-=4*z
			z=0
			break
for i in range(k):
	if arr[i]%2==0:
		seats-=arr[i]
	else:
		seats-=(arr[i]+1)
if seats<0:
	print "NO"
else:
	print "YES"


