#no. of zeros + identical 1's
myout=open("myout.txt","r+")
with open('input.txt',"r") as f:
	inp=[]
	for line in f:
		inp.append(line)
inp=[x.strip() for x in inp]
#t=int(input())
t=int(inp[0])
result=[]
for i in range(t):
	#n=int(input())
	n=int(inp[2*i+1])
	#arr=map(int,raw_input().split())
	arr=map(int,inp[2*i+2].split())
	#print arr
	c=n
	count2=0
	countid=0
	p2=-1
	res=0
	for m in range(n-1,-1,-1):
		if arr[m]==1:
			c=m
			break
	for m in range(n):
		if arr[m]==0:
			p2=m
			break
	#no. of zeros
	countz=0
	counto=0
	counto1=0
	for o in arr:
		if o==0:
			countz+=1
		else:
			counto+=1#count no. of one's
#	for o in range(p2,c):
		
#		counto1
	c3=0
	contz=0
	#continous zeros
	for w in range(p2,n):
		if arr[w]==0:
			contz+=1
		else:
			break
	counto-=p2
	tr=c-counto+1
	zx=0
	for i in range(p2,c):
		if arr[i]==0:
			zx-=1
		else:
			zx+=1
	#p2+=countz
	#count no. of ones special

	if c!=n and p2!=-1:
		#count no. of last 1's
		for x in range(c-1,p2-1,-1):
			if arr[x]==1:
				c3+=1
			else:
				break
		store=c
		#count no. of zeros before c and identicals
		for k in range(c-1,p2-1,-1):
			if (arr[k]==1 and arr[store]==1):
				countid+=1

			if arr[k]==0:
				count2+=1
			store-=1

		res=zx+tr
	result.append(res)
for i in result:
	#print i
	myout.write(str(i)+"\n")
			
