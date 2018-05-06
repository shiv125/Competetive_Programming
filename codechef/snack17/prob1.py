def fun(x,L):
	count=0
	tail=False
	x=list(x)
	z=[]
	for i in range(L):
		t=x.pop()
		if t!=".":
			z.append(t)
	if len(z)%2!=0:
		return False
	for i in range(0,len(z),2):
		if z[i]!='T':
			return False
	for i in range(1,len(z),2):
		if z[i]!='H':
			return False
	return True

t=input()
result=[]
for i in range(t):
	L=input()
	x=raw_input()
	result.append(fun(x,L))
	
for i in result:
	if i:
		print "Valid"
	else:
		print "Invalid"
