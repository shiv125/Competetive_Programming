import random
myout=open("testcases.txt","r+")
n=10000
myout.write(str(n)+"\n")
for i in range(n):
	myout.write(str(random.randint(1,10000))+" ")
