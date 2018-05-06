n,m,k=map(int,raw_input().split())
a=map(int,raw_input().split())
a.sort()
ck=0
count=0
m1=m
flag=0
i=0
while i<n:
	if a[i]<=m1:
		ck+=1
	else:
		#m1=m+a[i-]
		if ck>=k:
			count+=ck-k+1
			m1=m+a[i]
		else:
			m1=m+a[i]
			if a[i]==a[i-1]+1:
				ck=1
				i-=1
			else:
				ck=0
		#ck=0
		#m1=m+a[i-1]
		#if a[i-1]<=m1:
		#	ck=1
		#	i-=1
	i+=1
#print count
#print ck
if ck>=k:
	count+=ck-k+1
print count

