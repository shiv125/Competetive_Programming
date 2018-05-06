red=[]#n
blue=[]
k=0
a=0
b=0
slope=[a,b]
flag=0
while k<7:
	for i in range(n):
		xr,yr=red[i]
		if a*xr+b*yr<0:#y=1
			a=a+xr
			b=b+yr
			k+=1
	for j in range(m):
		xb,yb=blue[j]
		if a*xb+b*yb>=0:
			a=a+xb
			b=b+yb
			k+=1
	if k==0:
		break








