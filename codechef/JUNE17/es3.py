import math
a=math.exp(1)
y=1
for n in range(1,1100):
	t=0
	for i in range(n):
		t+=int(math.floor(a*(i+1)))
	w=math.floor(((n*(n+1))/2)*a)
	z=int(w-n/2)
	if abs(t-z)>1:
		print t,z



#if n<10**10:
#	print z
#else:
#	print z-2
'''
if n<=8:
	print z
elif n>8 and n<10**20:
	print z+1
elif n>=10**20 and n<10**10:
	print z-1
else:
	print z
'''

# 2 test cases right for ans==z for n between 1 to 10**10
