n,m=map(int,raw_input().split())
a=[]
b=[]
z=[0]*102
for i in range(102):
	z[i]=[]
for i in range(n):
	x,y=map(int,raw_input().split())
	z[x].append(y)
	#for j in range(x,y+1):
	#	count[j]+=1
an=[]
bn=[]
for i in range(102):
	if len(z[i])>0:
		z[i].sort()
		an.append(i)
		bn.append(z[i][-1])
p=len(an)
reach=bn[0]
#print p
#print an
#print bn

for i in range(1,p):
	if bn[i]>reach and an[i]<=reach:
	       reach=bn[i]
flag=0
if reach>=m:
	flag=1
if len(z[0])==0:
	flag=0
	       
if flag:
	print "YES"
else:
	print "YES"
