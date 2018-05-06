#no. of zeros + identical 1's
#myout=open("myout.txt","r+")
#with open('input.txt',"r") as f:
#	inp=[]
#	for line in f:
#		inp.append(line)
#inp=[x.strip() for x in inp]
t=int(input())
#t=int(inp[0])
result=[]
for i in range(t):
	n=int(input())
	#n=int(inp[2*i+1])
	arr=map(int,raw_input().split())
	#arr=map(int,inp[2*i+2].split())
	
	#find index of  first 0
	cf0=-1
	for j in range(n):
		if arr[j]==0:
			cf0=j
			break
	#find index of last 1
	cl1=-1
	for j in range(n-1,-1,-1):
		if arr[j]==1:
			cl1=j
			break
	temp=[]
	c=0
	store=cf0
	#count zero temp
	czt=0
	x1=[]
	sa=[]
	for j in range(cf0,cl1+1):
		c+=1
		if arr[j]==0:
			czt+=1
		if arr[j]==1:
			sa.append(czt)
			x1.append(j)
		if arr[j]==0 and arr[store]==1:
			temp.append(c-2)
			c=1
			#temp.append(i)
		store=j
	#print sa
	#print x1
	temp.append(c)
		
	#mantain of count of 0 by cof0
	cof=0
	#similarly count of 1 by cof1
	cof1=0
	max_=0
	H={}
	x=[]
	max_=0

	if (cf0!=-1 and cl1!=-1):
		for j in range(len(sa)):
			if sa[j]>max_:
				max_=sa[j]
			else:
				max_+=1

#	if (cf0!=-1 and cl1!=-1):
#		for i in range(len(temp)):
#			if temp[i]!=0:
#				if temp[i]>max_:
#					max_=temp[i]+1
#				else:
#					max_+=1
	#print temp
	#x.append(temp[0]-cf0)
	#for i in range(1,len(temp)):
	#	x.append(temp[i]-temp[i-1])
#	for m in x:
#		if m!=0:
#			if max_>m:
#				
#		else:
#			max_+=1
#	while True:
#		for i in range(cf0+,cl1+1):
#			if arr[cf0]==0:
#				cof+=1
#			else:
#				break
#		max_=max(cof,max_+1)
	
	result.append(max_)
for i in result:
	print i
	#myout.write(str(i)+"\n")
			

