n=input()
print "YES"
for i in range(n):
	x1,y1,x2,y2=map(int,raw_input().split(" "))
	if x1%2==0 and y1%2==0:
		print 1
	elif (x1%2==0 and y1%2!=0):
		print 2
	elif (x1%2!=0 and y1%2!=0):
		print 3
	else:
		print 4

