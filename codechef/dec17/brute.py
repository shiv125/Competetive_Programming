from math import sqrt
def sign(x1r,y1r,x2r,y2r,xb,yb):
	if x1r==x2r:
		fun=xb-x1r
	else:
		sl=((y2r-y1r)*1.0)/(x2r-x1r)
		fun=yb-y1r-sl*(xb-x1r)
	if fun>0:
		return 1
	elif fun==0:
		return 2
	else:
		return 0
t=input()
while t>0:
	t-=1
	n,m=map(int,raw_input().split())
	red=[]
	blue=[]
	for i in range(n):
		x,y=map(int,raw_input().split())
		red.append([x,y])
	for i in range(m):
		x,y=map(int,raw_input().split())
		blue.append([x,y])
	red.sort(key=lambda x:x[0])
	blue.sort(key=lambda x:x[0])
	slopes=[]
	max_cost=-1
	rp1=0
	rp2=0
	bp1=0
	bp2=0
	rp11=0
	rp22=0
	bp11=0
	bp22=0
	#l1=int(sqrt(n))/3
	#l2=int(sqrt(m))/3
	#l1=int(l1)
	#l2=int(l2)
	l1=1
	l2=1
	for i in range(0,n,l1):
		for j in range(0,n,l1):
			rp1=0
			rp2=0
			bp1=0
			bp2=0
			rp11=0
			rp22=0
			bp11=0
			bp22=0
			x1r,y1r=red[i]
			x2r,y2r=red[j]
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0:
					bp1+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)>=1:
					rp1+=1
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0 or sign(x1r,y1r,x2r,y2r,xb,yb)==2:
					bp11+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==1:
					rp11+=1
			
			##
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==1:
					bp2+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0 or sign(x1r,y1r,x2r,y2r,xb,yb)==2 :
					rp2+=1
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==1 or sign(x1r,y1r,x2r,y2r,xb,yb)==2:
					bp22+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0:
					rp22+=1
			max_cost=max(max_cost,rp1+bp1,rp2+bp2)
			max_cost=max(max_cost,rp11+bp11,rp22+bp22)
	print m+n-max_cost
	'''
	for i in range(0,m,l2):
		for j in range(0,m,l2):
			rp1=0
			rp2=0
			bp1=0
			bp2=0
			rp11=0
			rp22=0
			bp11=0
			bp22=0
			x1r,y1r=blue[i]
			x2r,y2r=blue[j]
			ma=-1
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0:
					bp1+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)>=1:
					rp1+=1
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0 or sign(x1r,y1r,x2r,y2r,xb,yb)==2:
					bp11+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==1:
					rp11+=1
			
			##
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==1:
					bp2+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0 or sign(x1r,y1r,x2r,y2r,xb,yb)==2 :
					rp2+=1
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==1 or sign(x1r,y1r,x2r,y2r,xb,yb)==2:
					bp22+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0:
					rp22+=1
			max_cost=max(max_cost,rp1+bp1,rp2+bp2)
			max_cost=max(max_cost,rp11+bp11,rp22+bp22)
	print m+n-max_cost

	for i in range(0,n,l1):
		for j in range(0,m,l2):
			rp1=0
			rp2=0
			bp1=0
			bp2=0
			rp11=0
			rp22=0
			bp11=0
			bp22=0
			x1r,y1r=red[i]
			x2r,y2r=blue[j]
			ma=-1
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0:
					bp1+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)>=1:
					rp1+=1
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0 or sign(x1r,y1r,x2r,y2r,xb,yb)==2:
					bp11+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==1:
					rp11+=1
			
			##
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==1:
					bp2+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0 or sign(x1r,y1r,x2r,y2r,xb,yb)==2 :
					rp2+=1
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==1 or sign(x1r,y1r,x2r,y2r,xb,yb)==2:
					bp22+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0:
					rp22+=1
			max_cost=max(max_cost,rp1+bp1,rp2+bp2)
			max_cost=max(max_cost,rp11+bp11,rp22+bp22)
	
	
	for i in range(0,m,l2):
		for j in range(0,n,l1):
			rp1=0
			rp2=0
			bp1=0
			bp2=0
			rp11=0
			rp22=0
			bp11=0
			bp22=0
			x1r,y1r=blue[i]
			x2r,y2r=red[j]
			ma=-1
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0:
					bp1+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)>=1:
					rp1+=1
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0 or sign(x1r,y1r,x2r,y2r,xb,yb)==2:
					bp11+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==1:
					rp11+=1
			
			##
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==1:
					bp2+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0 or sign(x1r,y1r,x2r,y2r,xb,yb)==2 :
					rp2+=1
			for k in range(m):
				xb,yb=blue[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==1 or sign(x1r,y1r,x2r,y2r,xb,yb)==2:
					bp22+=1
			for k in range(n):
				xb,yb=red[k]
				if sign(x1r,y1r,x2r,y2r,xb,yb)==0:
					rp22+=1
			max_cost=max(max_cost,rp1+bp1,rp2+bp2)
			max_cost=max(max_cost,rp11+bp11,rp22+bp22)

'''
#	print m+n-max_cost
		


					
