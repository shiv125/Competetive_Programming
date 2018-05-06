n,m=map(int,raw_input().split())
poland=[]
eball=[]
for i in range(n):
	poland.append(raw_input())
for i in range(m):
	eball.append(raw_input())
count=0
for i in poland:
	for j in eball:
		if i==j:
			count+=1
if (n==m):
	if (count%2==0):
		print "NO"
	else:
		print "YES"
if (n>m):
	print "YES"
if (n<m):
	print "NO"

