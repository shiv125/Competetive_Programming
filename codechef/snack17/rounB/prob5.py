t=input()
while t>0:
	t-=1
	n=input()
	start=[]
	end=[]
	for i in range(n):
		x1,y1,x2,y2=map(int,raw_input().split())
		start.append([x1,y1])
		end.append([x2,y2])
	x=10000
	y=10000
	x_ind=1
	y_ind=1
	for line in range(1,n+1):#xaxis
		z=0
		for i in range(n):
			z+=min(abs(start[i][0]-line),abs(end[i][0]-line))
		for yline in range(1,n+1):
			p=0
			for i in range(n):
				p+=min(abs(start[i][1]-yline),abs(end[i][1]-yline))
			if y>p:
				y=p
				y_ind=yline
		if x>z:
			x=z
			x_ind=line
	res=0
	print x,y
	for i in range(n):
		res=max(min(abs(start[i][0]-x_ind),abs(end[i][0]-x_ind)),min(abs(start[i][1]-y_ind),abs(end[i][1]-y_ind)),res)
	print res

			
				
		
