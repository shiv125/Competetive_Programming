n=input()
z=(n*(n+1))/2	
val=z/2
se=""
c=0
for i in range(n,0,-1):
	if val-i>=0:
		c+=1
		se+=str(i)
		se+=" "
		val-=i
if z%2:
	print 1
else:
	print 0
print c,
print se
	
