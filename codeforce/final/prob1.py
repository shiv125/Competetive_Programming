n=input()
arr=map(int,raw_input().split())
flag=0
flag2=0
if n==1:
	print "YES"
else:
	for i in range(n-1):
		if arr[i]==arr[i+1]:
			flag2=1
			break
	if flag2:		
		for i in range(n-1):
			if arr[i+1]<=arr[i]:
				break
		for j in range(i,n-1):
			if arr[j+1]!=arr[j]:
				break
		if arr[j+1]>arr[j]:
			flag=1
		else:
			j+=1
		for k in range(j,n-1):
			if arr[k+1]>=arr[k]:
				flag=1
				break
		if flag:
			print "NO"
		else:
			print "YES"

	else:
		flag3=0
		flag4=0
		for i in range(1,n-1):
			if arr[i+1]<arr[i]:
				break
		j=i+1
		for j in range(i+1,n-1):
			if arr[i+1]>arr[i]:
				break
		if j==n-1:
			print "YES"
		else:
			print "NO"

