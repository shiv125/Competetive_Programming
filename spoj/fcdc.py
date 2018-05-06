import math
a,b=map(int,raw_input().split())
c=b
d=a
lookup={}
lookup_a={}
mapr=1
pr=0
for i in range(2,int(math.floor(math.sqrt(b))+1)):
	if b%i==0:
		lookup[i]=0
		mapr=i
	while b%i==0:
		b=b/i
		lookup[i]+=1
if b>1:
	lookup[b]=1
for i in range(2,int(math.floor(math.sqrt(a))+1)):
	if a%i==0:
		lookup_a[i]=0
	while a%i==0:
		a=a/i
		lookup_a[i]+=1
if a>1:
	lookup_a[a]=1

'''
if shiv:
	elem=mapr
	count=lookup[elem]
	for i in range(elem,count*elem+1,elem):
		c1=0
		k=1
		while k/elem>0:
			k*=elem
			c1+=k/elem

		if c1==count:
			break
	print i-a
	print "s"
'''
c1=0	
flag=False
#for i in lookup:
#	print i
for j in range(1,d+1):
	flag=False
	for i in lookup_a:
		c1=0
		elem=1
		count=lookup_a[i]
		while j/elem>0:
			elem*=i
			c1+=j/elem
		if c1<count:
			flag=True
			break
	if flag==False:
		break
new_a=j




c1=0	
flag=False
total=0
#for i in lookup:
#	print i
for j in range(new_a,c):
	flag=False
	for i in lookup:
		c1=0
		elem=1
		count=lookup[i]
		while j/elem>0:
			elem*=i
			c1+=j/elem
		if c1<count:
			flag=True
			break
	if flag==True:	
		total+=1
	else:
		break
print total

