import math


a=math.exp(1)
a1=a/(a-1)
n=input()
t=0
#w=math.floor(((n*(n+1))/2)*a)
#z=int(w-n/2)
#n1=int(math.floor(a*(n)))


for i in range(n):
	t+=int(math.floor(a*(i+1)))	
	#t2=int(math.floor(a*(i+2)))	
	#result.append(t2-t1)
print t

'''
n2=(12*n1+1)/19
total=((n1+1)*n1)/2
result=[]
for i in range(1,10):
	if (int(math.floor((19*i-1)/12))-int(math.floor(a1*(i))))!=0:
		print str(i)+'s'
for i in range(1,13):
	result.append(int(math.floor((19*i-1)/12)))
print result
ans=0
su=sum(result)
t=n2/12
ans=t*su+19*12*(t-1)
if n2>67:
	ans+=105-int(math.floor((19*67-1)/12))
print total-ans
'''
