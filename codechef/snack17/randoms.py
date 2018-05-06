import random
myout=open("testcases.txt","w+")
t=10000
#myout.write("5\n")
for i in range(t):
	#n=random.randint(10,100)
	#n=random.randint(10**5-1,10**5)
	n=70
	#q=random.randint(10**5-1,10**5)
	q=1
	myout.write(str(n)+" "+str(q)+"\n")
	for m in range(n):
		x=random.randint(10,1000)
		myout.write(str(x)+" ")
	myout.write("\n")
	for m in range(q):
		z=random.randint(11,10**4)
		myout.write(str(z)+"\n")

	
