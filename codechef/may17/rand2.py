import random
myout=open("codet.txt","r+")
t=13
for m in range(t):
	N=random.randint(1,10)
	M=random.randint(1,20)
	myout.write(str(N)+" "+ str(M)+"\n")
	for i in range(N):
		x=random.randint(1,20)
		myout.write(str(x)+" ")
	myout.write("\n")


