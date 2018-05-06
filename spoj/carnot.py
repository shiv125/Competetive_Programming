MAX=4473
MA=10**7+4
i=1
count=2
store=[0]*(10**7+10)
store[1]=[1,1]
store[2]=[2,1]
while i<MAX:
	k=0
	for j in range(i-1,-1,-1):
		count+=1
		if count>=MA:
			break
		k+=1
		store[count]=[j+1,k+1]
	j=0
	count+=1	
	k=i
	if count==MA:
		break
	store[count]=[1,i+2]
	i+=1

	for j in range(1,i+1):
		count+=1
		if count>=MA:
			break

		store[count]=[j+1,k+1]
		k-=1
	i+=1
	count+=1
	if count>=MA:
		break
	if i<MAX:
		store[count]=[i+1,1]
t=input()
while t>0:
	t-=1
	n=input()
	a,b=store[n]
	print "TERM "+str(n)+ " IS "+str(b)+"/"+str(a)

	
		
