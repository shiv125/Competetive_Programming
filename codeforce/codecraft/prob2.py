def gcd(a,b):
	if (b==0):
		return a
	else:
		return gcd(b,a%b)



N=input()
arr=map(int,raw_input().split(' '))
max_=0
for i in range(N):
	count=0
	for j in range(N):
		k=gcd(arr[i],arr[j])
		print k
		
		if (k!=1):
			count+=1
	print "\n"
	max_=max(count,max_)
		
print max_
