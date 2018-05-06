import math
a=math.exp(1)
n=400
t=0
result=[]
z=n/7

for i in range(n):
	t+=int(math.floor(a*(i+1)))	
	#t2=int(math.floor(a*(i+2)))	
	#result.append(t2-t1)
print t

t=(n-2)/7
ans=7+111*t+19*7*t*(t-1)/2
rem=(n-2)%7
if rem==1:
	ans+=8+19*t
elif rem==2:
	ans+=18+38*t
elif rem==3:
	ans+=31+57*t
elif rem==4:
	ans+=47+76*t
elif rem==5:
	ans+=66+95*t
elif rem==6:
	ans+=87+114*t
print ans
