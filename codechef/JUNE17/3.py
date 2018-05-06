import math
a=math.e

for n in range(1,100):
	t=0
	for i in range(n):
		t+=int(math.floor(a*(i+1)))
	w=math.floor(((n*(n+1))/2)*a)
	z=int(w-n/2)
	if abs(t-z)>0:
		print (t,z)
