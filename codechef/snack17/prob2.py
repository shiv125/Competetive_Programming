def fun(arr,n):
	if n%2==0:
		return False
	elem=0
	for i in range(n/2+1):
		elem+=1
		if elem!=arr[i]:
			return False
	for i in range(n/2,n):
		if elem!=arr[i]:
			return False
		elem-=1
	return True
		

t=input()
result=[]
for i in range(t):
	n=input()
	arr=map(int,raw_input().split())
	result.append(fun(arr,n))
for i in result:
	if i:
		print "yes"
	else:
		print "no"
