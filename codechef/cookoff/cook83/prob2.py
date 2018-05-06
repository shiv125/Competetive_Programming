t=input()
while t>0:
	t-=1
	n=input()
	print n
	y=0
	for i in range(n):#rounds
		print n
		if y==0:
			for j in range(n):
				print j+1,1,n
		else:
			for j in range(n):
				print j+1,y,y+1
		y+=1

