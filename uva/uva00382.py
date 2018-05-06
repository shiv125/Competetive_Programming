import math
import random
def propdev(n):
	res=0
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			if i==n//i:
				res+=i
			else:
				res+=(i+n/i)
	t=res+1
	if t==n:
		return 0#perfect
	elif t>n:
		return 1#abundant
	else:
		return -1
arr=list(map(int,input().split()))
print ('PERFECTION OUTPUT')
for i in range(len(arr)-1):
	t=propdev(arr[i])
	s=str(arr[i])
	l=len(s)
	e=5-len(s)
	z=''
	for j in range(e):
		z+=' '
	z+=s
	if arr[i]==1:
		print (z,' DEFICIENT')
	else:
		if t==0:
			print (z,' PERFECT')
		elif t==1:
			print (z,' ABUNDANT')
		else:
			print (z,' DEFICIENT')

print ('END OF OUTPUT')
