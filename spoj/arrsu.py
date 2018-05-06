n=input()
arr=map(int,raw_input().split())
k=input()
res=[]
m1=-1
m2=-1
c=0
for i in range(k):
	m1=max(m1,arr[i])
for i in range(k):
	if arr[i]!=m1:
		m2=max(m2,arr[2])
	if arr[i]==m1:
		c+=1
if c>1:
	m2=m1
for i in range(k,n-1):
	if arr[i]>m1:
		m1=arr[i]
	if arr[i+1]>m2:
		m2=arr[i+1]
		
	ma=-1
	for j in range(i,i+k):
		ma=max(ma,arr[j])
	print ma,	

