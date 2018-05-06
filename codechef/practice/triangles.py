import time
import math
def comp(x,y):
	if x[0]==y[0]:
		if x[1]>y[1]:
			return 1
		elif x[1]<y[1]:
			return -1
		else:
			if x[2]>y[2]:
				return 1
			else:
				return -1
	return 0
R=input()
y=4*R*R
flag=False
count=0
arr=[]
temp=set()
let=[]

for x in range(1,int(2*R*1.733)+1):
	a=(4*R*R-2*R*(int(math.sqrt(4*R**2+x*x))))/x
	b=(4*R*R+2*R*(int(math.sqrt(4*R**2+x*x))+1))/x	
	a=max(1,a)
	for y in range(a,b+1):
		if x*y!=4*R*R and y>0:
			z=(4*R*R*(x+y))/(x*y-4*R*R)
			let=sorted([x,y,z],reverse=True)
			if z>0:
				temp.add((let[0],let[1],let[2]))

for i in temp:
	p=sum(i)/2
	a=(2*p-i[0])/2
	b=(2*p-i[1])/2
	c=(2*p-i[2])/2
	if (a+b-c)*(b+c-a)*(c+a-b)==(a+b+c)*4*R*R:
		arr.append([a,b,c])
arr=sorted(arr,key=lambda x:x[0])
arr=sorted(arr,cmp=comp)
print len(arr)
#print len(temp)
#print count
'''
for a in range(1,MAX):
	for b in range(a+1,MAX):
		for c in range(b+1,b+a):
			#if (a+b)>c and (b+c)>a and (c+a)>b:
			#	flag=True
			if (a+b-c)*(b+c-a)*(c+a-b)==(a+b+c)*y:
				count+=1
				arr.append([a,b,c])

for a in range(1,MAX):
	for b in range(a+1,2*a):
		if (a*b-(b*b)/2)**2==(4*a*a-b*b)*R*R:
			count+=1
			arr.append([a,a,b])
for a in range(1,MAX):
	if a*a==12*R*R:
		count+=1
		arr.append([a,a,a])
print count
'''
for i in arr:
	print ' '.join(str(x) for x in i)


