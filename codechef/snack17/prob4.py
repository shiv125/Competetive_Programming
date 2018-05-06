def fun(x11,y11,x12,y12,x21,y21,x22,y22):
	#for same rows
	t1=min(x11,x12)
	t2=max(x11,x12)
	x11=t1
	x12=t2
	t1=min(x21,x22)
	t2=max(x21,x22)
	x21=t1
	x22=t2
	if y11==y12:
		if y21==y22 and y12==y21:
			if x11<x21:
				if max(x11,x12)-min(x21,x22)>=0:
					return True
			else:
				if max(x21,x22)-min(x11,x12)>=0:
					return True
		else:
			if x12==x22 or x11==x22:
				if y11==y21 or y11==y22:
					return True
	return False		
t=input()
result=[]
for i in range(t):
	res=0
	x11,y11,x12,y12=map(int,raw_input().split())
	x21,y21,x22,y22=map(int,raw_input().split())
	if x11==x12 and x12==x21 and x21==x22:#if both are cols rotate the two arrays
		res=fun(y11,1,y12,1,y21,1,y22,1)
		#x12=y12
		#x21=y21
		#x22=y22
		#y12=y11
		#y21=y11
		#y22=y11
	else:
		if y11!=y12:
			res=fun(x21,y21,x22,y22,x11,y11,x12,y12)	
						#swap the points
		else:
			res=fun(x11,y11,x12,y12,x21,y21,x22,y22)
	result.append(res)
	#for same rows
for i in result:
	if i:
		print "yes"
	else:
		print "no"
