import random
myout=open("test1.txt","r+")
t=13
for m in range(t):
	N=random.randint(1,15)
	K=random.randint(1,15)
	P=random.randint(1,15)
	arr=[]
	y=[]
	for i in range(N):
		arr.append(str(random.randint(0,1)))
		arr.append(" ")
	for i in range(P-1):
		y.append('!')
	y.append('?')
	arr=''.join(arr)
	y=''.join(y)
	myout.write(str(N)+' '+ str(K)+' '+str(P)+"\n")
	myout.write(arr+"\n")
	myout.write(y+"\n")

