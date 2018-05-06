def fun(N,K):# if n is odd
	r=2
	N=N+2
	arr=[0]*N
	arr[0]=1
	arr[-1]=1
	x=[]
	s=0
	y=[]
	while K>0:
		for z in range(1,(r/2)+1):
			#x.append(2**z-1)
			#y.append(2**r)
			a=2*z-1
			b=r
			t=(a*N)/b
			arr[t]=1
			x.append(t)
			K-=1
			if K==0:
				l=t
				break
		r=2*r
	for i in range(t-1,-1,-1):
		if arr[i]==1:
			s=i
			break
	left=t-s-1
	for i in range(t+1,N):
		if arr[i]==1:
			break
	right=i-t-1
	left=max(left,0)
	right=max(right,0)
	ma=max(left,right)
	mi=min(left,right)
	return ma,mi,x
myout3=open("fin.txt","a")
with open('mytestcases.txt',"r") as f:
	inp=[]
	for line in f:
		inp.append(line)
inp=[x.strip() for x in inp]
t=int(inp[0])
#1 for filled
#0 for empty
for ind in range(1,t+1):
	N,K=map(int,inp[ind].split())
	if N%2!=0:
		if K<=(N+1)/2:
			ma,mi,x=fun(N,K)
			#print arr
		else:
			mi=0
			ma=0
	else:
		if K<=(N-1)/2:
			ma,mi,x=fun(N,K)
		elif K==N/2:
			ma=1
			mi=0
		else:
			mi=0
			ma=0
	print x
	print ma, mi
	myout3.write("Case #"+str(ind)+": "+str(ma)+" "+str(mi)+"\n")

