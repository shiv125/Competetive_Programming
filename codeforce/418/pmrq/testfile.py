import random
myout=open("testc2.txt","r+")
#n=random.randint(1000,10**5)
n=10**5
myout.write(str(n)+"\n")
#print n
#m=random.randint(1000,10**5)
m=10**5
for i in range(n):
	myout.write(str(random.randint(1,10**6))+" ")
myout.write("\n"+str(m)+"\n")
for i in range(m):
	l=random.randint(1,n)
	x=random.randint(1,10**6)
	y=random.randint(2,10**6)
	r=random.randint(1,n)
	if r<l:
		r=l

	if y<x:
		y=x
	myout.write(str(l)+" "+str(r)+" "+ str(2)+" "+ str(y)+"\n")

