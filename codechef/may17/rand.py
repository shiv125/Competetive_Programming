import random
myout=open("codetest.txt","r+")
t=10
ax='abcdefghijklmnopqrstuvwxyz'
ab='-+'
for m in range(t):
	N=random.randint(1,10)
	temp=''
	myout.write(str(N)+"\n")
	for k in range(N):
		temp=''
		q=random.randint(0,1)
		temp+=str(ab[q])
		temp+=" "
		l=random.randint(1,32)
		for j in range(l):
			w=random.randint(0,25)
			temp+=str(ax[w])
		#temp=''.join(temp)
		myout.write(temp+"\n")
	
