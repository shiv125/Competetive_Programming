def sumofdigits(i):
	t=0
	while i>0:
		t+=i%10
		i=i/10
	return t
def binarysearchfloor(low,high,x):
	while high-low>1:
		mid=(low+high)/2
		if mid-sumofdigits(mid)<=x:
			low=mid
		else:
			high=mid
	if low+1-sumofdigits(low+1)<x:
		return low+1
	return low
n,s=map(int,raw_input().split())
count=0
if s>=n:
	count=n
else:
	count=binarysearchfloor(1,n,s-1)
print n-count
