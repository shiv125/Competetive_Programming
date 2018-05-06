import numpy as np
t=0
def sun(a,b):
	#a1=numpy.array(a)
	#b1=numpy.array(b)
	rem=np.polydiv(a,b)[1]
	return rem
def fun(a,b):
	global t
	if len(b)==1 and b==0:
		return a
	else:
		t+=1
		return fun(b,sun(a,b))


n=input()
x=[0]*(n+1)
y=[0]*(n)
if n==1:
	print 1
	print 0,1
	print 0
	print 1
else:
	for i in range(n,-1,-3):
		x[i]=1
		x[i-1]=0
		x[i-2]=-1

	rem=(n+1)%3
	if rem==1:
		x[0]=1
	if rem==2:
		x[1]=1
		x[0]=0
	for i in range(n-1,-1,-3):
		y[i]=1
		y[i-1]=0
		y[i-2]=-1
	rem=n%3
	if rem==1:
		y[0]=1
	if rem==2:
		y[1]=1
		y[0]=0
x=[0,1,-1,0,1]
y=[0,0,0,1]
x=np.array(x)
y=np.array(y)
fun(x,y)
print t
	#print n
	#print " ".join(str(z) for z in x)
	#print n-1
	#print " ".join(str(z) for z in y)

