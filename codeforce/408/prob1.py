n,m,k=map(int,raw_input().split())
arr=map(int,raw_input().split())
left=1000
right=1000
for i in range(m):
	if k-arr[i]>=0 and arr[i]!=0:
		left=min(left,abs(i-(m-1)))
for i in range(m,n):
	if k-arr[i]>=0 and arr[i]!=0:
		right=min(right,abs(i-(m-1)))

print 10*min(left,right)
