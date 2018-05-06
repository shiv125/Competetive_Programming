a='Shakes*e'
b='Sh*speare'
a='*bcdab'
b='*a'
n=len(a)
count=0
for i in a:
	if i=='*':
		count+=1
		
n=4*count+n
i=0
j=0
c=0
while i<n:
	if a[i]=='*':
		j+=1
		c=4
	elif b[j]=='*':
		i+=1
	else:
		if a[i]!=b[j]:
			return False
		else:
			i+=1
			j+=1
	i+=1
	j+=1
