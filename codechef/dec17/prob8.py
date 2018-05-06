t=input()
while t>0:
	t-=1
	N,G,B,X,Y=map(int,raw_input().split())
	P=map(int,raw_input().split())
	z=[]
	for i in range(N):
		z.append(map(int,raw_input().split())) 
	for i in range(N):
		xi,yi,ki,li=z[i]
		print 2,li
		print 1,i+1
		print 3,li
		print 2,ki
		print 1,0
		print 3,ki
	print 0
