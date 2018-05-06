#with open('output_correct.txt',"r") as f0:
#	inp=[]
#	for line in f0:
#		inp.append(line)
#inp=[x.strip() for x in inp]
j=0
t=input()
while t>0:
	t-=1
	X,Y,Z,A,B,C=map(int,raw_input().split())
	x=min(X,Y,Z)
	lis=sorted([X,Y,Z])
	cost=0
	rest=[100000000]*9
	rest[0]=A*(sum(lis))
	
	#if lis[0]+lis[2]==2*lis[1]:
	#		q1=(3*lis[1]*B)/2
	#		if q1*2==3*lis[1]*B:
	#			e=q1
	#			rest[1]=e
	habbi=lis[0]+lis[1]+lis[2]
	if (habbi)%2==0:
		if habbi-(lis[1]+lis[2])==lis[0]:
			if habbi/2>lis[2]:
				rest[1]=(habbi/2)*B
	
	if X==Y and Y==Z:
		rest[2]=C*X
	temp=lis[0]+lis[1]
	temp=min(temp,lis[2])
	tot=0
	tot+=temp*B
	tot+=(sum(lis)-2*temp)*A
	rest[3]=tot
	tot=min(lis)*C
	tot+=(sum(lis)-3*min(lis))*A
	rest[4]=tot
	
	tot=0
	tot=C
	lis1=[0]*3
	for i in range(3):
		lis1[i]=lis[i]-1
	temp=lis1[0]+lis1[1]
	temp=min(temp,lis1[2])
	tot+=temp*B
	#print tot
	tot+=(sum(lis1)-2*temp)*A
	#print tot
	rest[5]=tot
	lis1=[0]*3
	tot=0
	for i in range(3):
		lis1[i]=lis[i]-1
	tot=C
	habbi=lis1[0]+lis1[1]+lis1[2]
	if (habbi)%2==0:
		if habbi-(lis1[1]+lis1[2])==lis1[0]:
			if habbi/2>lis1[2]:
				tot+=(habbi/2)*B
				rest[6]=tot
	tot=0
	#if sum(lis1)%2==0:
	#	tot+=
	z=min(X,Y,Z)
	temp=lis[2]-z-(lis[1]-z)

	tot+=(z-temp)*C
	if z-temp>=0:
		temp=(temp+lis[2]-z)*B
		#print str(temp)+"as"
		tot+=temp
		rest[7]=tot
	#print rest
	tot=A
	lis1=[0]*3
	lis1[0]=lis[0]
	lis1[1]=lis[1]
	lis1[2]=lis[2]-1
	habbi=lis1[0]+lis1[1]+lis1[2]
	if (habbi)%2==0:
		if habbi-(lis1[1]+lis1[2])==lis1[0]:
			if habbi/2>lis1[2]:
				tot+=(habbi/2)*B
				rest[8]=tot

	ew=min(rest)
	print rest
	if x%2==0:
		cost=min(C*x,3*A*x,(3*B*x)/2)
		m=lis[1]-x
		n=lis[2]-x
		temp=min(A*m+A*n,B*min(m,n)+A*(max(m,n)-min(m,n)))
		w=temp+cost
		e=w
		if lis[0]+lis[2]==2*lis[1]:
			q1=(3*lis[1]*B)/2
			if q1*2==3*lis[1]*B:
				e=w
			
		fin= min(e,w,ew)
	else:
		x-=1
		cost=min(C*x,3*A*x,(3*B*x)/2)
		c1=0
		c2=0
		c3=0
		m1=lis[1]-x
		n1=lis[2]-x-1
		c1=min(A*m1+A*n1,B*min(m1,n1)+A*(max(m1,n1)-min(m1,n1)))+B
		#print str(c1)+"hehe"
		m2=m1-1
		n2=n1
		c2=min(A*m2+A*n2,B*min(m2,n2)+A*(max(m2,n2)-min(m2,n2)))+C
		#print str(c2)+"he"
		m3=lis[1]-x
		n3=lis[2]-x
		c3=min(A*m3+A*n3,B*min(m3,n3)+A*(max(m3,n3)-min(m3,n3)))+A
		#print str(c3)+"d"
		w=cost+min(c1,c2,c3)
		e=w
		if lis[0]+lis[2]==2*lis[1]:
			q1=(3*lis[1]*B)/2
			if q1*2==3*lis[1]*B:
				e=w	
		fin= min(e,w,ew)
	#if fin!=int(inp[j]):
		#print j,fin,inp[j]
	print fin

	j+=1

