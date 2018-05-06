n=input()
arr=[0]*n
for i in range(n):
	arr[i]=map(int,raw_input().split())
done=0
flag=True
for i in range(n):
	for j in range(n):
		if arr[i][j]!=1:
			flag=False
			for k in range(n):
				for l in range(n):
					if arr[i][k]+arr[l][j]==arr[i][j] and k!=j and l!=i:
						flag=True
			if flag==False:
				done=1
				break
	if done==1:
		break
if done:
	print "No"
else:
	print "Yes"
