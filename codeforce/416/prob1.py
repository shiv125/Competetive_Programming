import math
a,b=map(int,raw_input().split())
n=math.floor(math.sqrt(a))
if b<n*(n+1):
	print "Valera"
else:
	print "Vladik"
