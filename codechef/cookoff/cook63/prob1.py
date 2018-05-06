t=input()
result=[]
while t>0:
	t-=1
	n=input()
	flag=0
	arr=map(int,raw_input().split())
	for i in range(1,n):
		if arr[i]<arr[i-1]:
			temp=arr[i]
			arr[i]=arr[i-1]
			arr[i-1]=temp
	for i in range(1,n):
		if arr[i]<arr[i-1]:
			flag=1
	result.append(flag)
for flag in result:
	if flag:
		print "NO"
	else:
		print "YES"

