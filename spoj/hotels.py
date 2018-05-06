n,m=map(int,raw_input().split())
arr=map(int,raw_input().split())
ma=arr[0]
cm=arr[0]
for i in range(1,n):
	if cm+arr[i]>m:
		cm=arr[i]
	else:
		cm+=arr[i]
	if cm<=m and cm>ma:
		ma=cm
print ma

