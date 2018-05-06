x1,y1,x2,y2=map(int,raw_input().split())
a,b=map(int,raw_input().split())
flag=0
if (x2-x1)%(2*a)==0 and (y2-y1)%(2*b)==0: 
	flag=1
if (x2-x1-a)%(2*a)==0 and (y2-y1-b)%(2*b)==0: 
	flag=1

if flag:
	print "YES"
else:
	print "NO"
	

