arr=[-7,10,9,2,3,8,8,6]
n=len(arr)
lookup=[1]*n
back=[-1]*n
for i in range(1,n):
	for j in range(i):
		if arr[i]>arr[j] and lookup[i]<lookup[j]+1:
			lookup[i]=lookup[j]+1
			back[i]=j
		
max_=max(lookup)
i=lookup.index(max_)
final=[]
while i>=0:
	final.append(arr[i])
	i=back[i]
final=sorted(final)
print final


