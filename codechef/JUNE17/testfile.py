import random
n=random.randint(1,10)
print n
m=random.randint(1,10)
for i in range(n):
	print random.randint(1,20),
print
print m
for i in range(m):
	l=random.randint(1,n)
	print l,
	r=random.randint(1,n)
	if r<l:
		r=l
	print r,
	print 2,
	print 16,
	print

